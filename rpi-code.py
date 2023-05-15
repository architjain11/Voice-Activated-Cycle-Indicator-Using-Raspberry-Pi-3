"""
Connect a resistor and LED to board pin 8 and run this script.
Whenever you say "stop", the LED should flash briefly
"""

import sounddevice as sd
import numpy as np
import scipy.signal
import timeit
import python_speech_features
from gpiozero import LED
from tflite_runtime.interpreter import Interpreter

# Parameters
debug_time = 0
debug_acc = 0
led_left=LED(26)
led_right=LED(6)
blink_duration=20 # double of time the led blinks
flag=2*blink_duration
word_threshold = 0.5
rec_duration = 0.5
window_stride = 0.5
sample_rate = 48000
resample_rate = 8000
num_channels = 1
num_mfcc = 16
stop_model_path = 'stop.tflite'
right_model_path = 'right.tflite'
left_model_path = 'left.tflite'

# Sliding window
window = np.zeros(int(rec_duration * resample_rate) * 2)

# Load model (interpreter)
stop_interpreter = Interpreter(stop_model_path)
stop_interpreter.allocate_tensors()
input_details = stop_interpreter.get_input_details()
output_details = stop_interpreter.get_output_details()
print(input_details)

right_interpreter = Interpreter(right_model_path)
right_interpreter.allocate_tensors()
input_details = right_interpreter.get_input_details()
output_details = right_interpreter.get_output_details()
print(input_details)

left_interpreter = Interpreter(left_model_path)
left_interpreter.allocate_tensors()
input_details = left_interpreter.get_input_details()
output_details = left_interpreter.get_output_details()
print(input_details)

# Decimate (filter and downsample)
def decimate(signal, old_fs, new_fs):

    # Check to make sure we're downsampling
    if new_fs > old_fs:
        print("Error: target sample rate higher than original")
        return signal, old_fs

    # We can only downsample by an integer factor
    dec_factor = old_fs / new_fs
    if not dec_factor.is_integer():
        print("Error: can only decimate by integer factor")
        return signal, old_fs

    # Do decimation
    resampled_signal = scipy.signal.decimate(signal, int(dec_factor))

    return resampled_signal, new_fs

# This gets called every 0.5 seconds
def sd_callback(rec, frames, time, status):

    led_left.off()
    led_right.off()

    global flag

    # Start timing for testing
    start = timeit.default_timer()

    # Notify if errors
    if status:
        print('Error:', status)

    # Remove 2nd dimension from recording sample
    rec = np.squeeze(rec)

    # Resample
    rec, new_fs = decimate(rec, sample_rate, resample_rate)

    # Save recording onto sliding window
    window[:len(window)//2] = window[len(window)//2:]
    window[len(window)//2:] = rec

    # Compute features
    mfccs = python_speech_features.base.mfcc(window,
                                             samplerate=new_fs,
                                             winlen=0.256,
                                             winstep=0.050,
                                             numcep=num_mfcc,
                                             nfilt=26,
                                             nfft=2048,
                                             preemph=0.0,
                                             ceplifter=0,
                                             appendEnergy=False,
                                             winfunc=np.hanning)
    mfccs = mfccs.transpose()

    # Make prediction from model
    in_tensor = np.float32(mfccs.reshape(1, mfccs.shape[0], mfccs.shape[1], 1))
    stop_interpreter.set_tensor(input_details[0]['index'], in_tensor)
    stop_interpreter.invoke()
    output_data = stop_interpreter.get_tensor(output_details[0]['index'])
    stop_val = output_data[0][0]

    in_tensor = np.float32(mfccs.reshape(1, mfccs.shape[0], mfccs.shape[1], 1))
    left_interpreter.set_tensor(input_details[0]['index'], in_tensor)
    left_interpreter.invoke()
    output_data = left_interpreter.get_tensor(output_details[0]['index'])
    left_val = output_data[0][0]

    in_tensor = np.float32(mfccs.reshape(1, mfccs.shape[0], mfccs.shape[1], 1))
    right_interpreter.set_tensor(input_details[0]['index'], in_tensor)
    right_interpreter.invoke()
    output_data = right_interpreter.get_tensor(output_details[0]['index'])
    right_val = output_data[0][0]

    if stop_val > word_threshold:
        print('stop')
        flag=blink_duration*2

    if right_val > word_threshold:
        print('right')
        flag=0

    if left_val > word_threshold:
        print('left')
        flag=blink_duration/2

    if flag<blink_duration/2:
        led_right.on()
        flag+=1
        if(flag==blink_duration/2): flag=blink_duration*2
    elif flag<blink_duration:
        led_left.on()
        flag+=1

    if debug_acc:
        print("stop:", end="")
        print(stop_val, end=" ")
        print("right:", end="")
        print(right_val, end=" ")
        print("left:", end="")
        print(left_val)

    if debug_time:
        print(timeit.default_timer() - start)


# Start streaming from microphone
with sd.InputStream(channels=num_channels,
                    samplerate=sample_rate,
                    blocksize=int(sample_rate * rec_duration),
                    callback=sd_callback):
    while True:
        pass

