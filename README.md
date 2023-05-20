# Voice Activated Cycle Indicator using Raspberry Pi 3

## Aim
Build a project by utilising TinyML/TensorFlow library on a single board computer/ microcontroller.

## Hardware Required
Raspberry Pi 3 Model B, Breadboard, Jumper Wires, LEDs, Resistors, Microphone (Raspberry Pi USB 2.0 Mini Microphone), Power Bank And Cable For Power Supply 

## Software Requried
Raspberry Pi Imager, Remote Desktop Connection, Putty For SSH Configuration Via Wi-Fi, Thonny Python IDE On Pi OS, Jupyter Notebooks For Pre-Processing And Model Training 

## Project Overview
Voice-activated cycle indicator lights are an innovative and efficient way to ensure cyclist safety on the road. This project aims to enhance the visibility of cyclists on the road and increase road safety, especially at night or in low light conditions. The system comprises a microphone, a voice recognition TensorFlow Lite model, a Raspberry Pi 3, and LED lights. The microphone captures the user's voice, and the voice recognition module processes the user's commands. The Raspberry Pi is responsible for controlling the LED lights based on the user's voice commands. The system's main functionality is to indicate the cyclist's turning direction by activating the appropriate LED strips. The user can activate the left or right turn signal by saying "left" or "right" respectively. Once the command is recognized, the corresponding LEDs will light up, indicating the cyclist's intention to turn. The indicator lights blink 10 times before automatically coming to a stop. In addition, the “stop” word will immediately stop all LEDs from blinking even before the 10 blinks. The voice recognition module uses a machine learning algorithm CNN (Convolutional Neural Network) that has been trained to recognize specific voice commands. The system has been designed to be user-friendly, and the voice commands are simple and easy to remember. The embedded system will also be quite energy efficient. The system can be attached to the bike using adhesive tape or cable ties, and the microphone and the embedded hardware can be mounted on the bike frame.

## Workflow

![directories](/assets/workflow.png)

The extraction.ipynb notebook is used to extract features from the Google Speech Commands Dataset (2.26GB). The output of feature extraction is the all_targets_mfcc_sets.npz file.
The three model training files modeltrainingleft.ipypnb, modeltrainingright.ipypnb and modeltrainingleft.ipypnb train the words “left”, “right”, and “stop” respectively using the features extracted in the .npz file from the first step. The output of training the CNN model is the model itself namely, left.h5, right.h5 and stop.h5.
The convert_tflite.ipypnb notebook converts the models in .h5 extension to a TensorFlow Lite file which is more suitable to run on embedded systems. The output files are left.tflite, right.tflite and stop.tflite respectively.
The .tflite files are imported in the python code rpi-code.py which is running on the Raspberry Pi 3 itself. LEDs are connected to the GPIO pins on the raspberry pi and input from microphone (window size 0.5 seconds) is used to make prediction and blink the indicator lights or LEDs when invoked.

Raspberry Pi OS can be viewed either by connecting through HDMI cable or via Wi-Fi. In this project, Remote Desktop Connection is used to see the Pi OS graphic interface on which we use the Thonny Python IDE to run the code. It should be notes that even without the connection to a physical display, the code would be automatically running, so, no issue should arise by mounting it directly on the cycle without a physical display. As soon as Pi receives power and boots up, the program starts running itself.

![desktop](/assets/desktop.png)

The left LED is connected to the GPIO Pin 26 (purple wire) and the right LED to GPIO Pin 6 (blue wire). The third wire (grey wire) is connected to ground. The circuit diagram of the connections can be shown below:

![connections](/assets/connections.jpg)

## Output

Raspberry Pi code is executed and we can observe that model is trained the word recognized is displayed on the screen.

![output screen](/assets/output.png)

The corresponding LED blinks 10 times to indicate the cyclist’s intention to turn. This can be seen on the prototype successfully implemented.

![demo](/assets/demo.jpg)

If you speak the "right" command, the right LED starts blinking, and if you immediately change the command by speaking “left”, the left LEDs begin blinking right away stopping the earlier command. This is to ensure that if by mistake wrong direction was specified by the user, it can be overridden to indicate the correct one.

https://github.com/architjain11/Voice-Activated-Cycle-Indicator-Using-Raspberry-Pi-3/assets/63463358/0b1bf32c-d635-443f-9406-495c9ce5ed11

## Conclusion
In conclusion, the voice-activated cycle indicator lights project is a simple and effective solution to improve cyclist safety on the road. The system's voice-activated commands make it easy for cyclists to use, and the LEDs provide excellent visibility to other road users. The project's potential to enhance road safety and reduce cycling accidents makes it a valuable addition to any cyclist's gear.
