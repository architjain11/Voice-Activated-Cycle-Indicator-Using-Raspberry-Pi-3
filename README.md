# Voice Activated Cycle Indicator using Raspberry Pi 3 Model B

## AIM
Build a project by utilising TinyML/TensorFlow library on a single board computer/ microcontroller.

## Hardware Required
Raspberry Pi 3 Model B, Breadboard, Jumper Wires, LEDs, Resistors, Microphone (Raspberry Pi USB 2.0 Mini Microphone), Power Bank And Cable For Power Supply 

## Software Requried
Raspberry Pi Imager, Remote Desktop Connection, Putty For SSH Configuration Via Wi-Fi, Thonny Python IDE On Pi OS, Jupyter Notebooks For Pre-Processing And Model Training 

## Project Overview
Voice-activated cycle indicator lights are an innovative and efficient way to ensure cyclist safety on the road. This project aims to enhance the visibility of cyclists on the road and increase road safety, especially at night or in low light conditions. The system comprises a microphone, a voice recognition TensorFlow Lite model, a Raspberry Pi 3, and LED lights. The microphone captures the user's voice, and the voice recognition module processes the user's commands. The Raspberry Pi is responsible for controlling the LED lights based on the user's voice commands. The system's main functionality is to indicate the cyclist's turning direction by activating the appropriate LED strips. The user can activate the left or right turn signal by saying "left" or "right" respectively. Once the command is recognized, the corresponding LEDs will light up, indicating the cyclist's intention to turn. The indicator lights blink 10 times before automatically coming to a stop. In addition, the “stop” word will immediately stop all LEDs from blinking even before the 10 blinks. The voice recognition module uses a machine learning algorithm CNN (Convolutional Neural Network) that has been trained to recognize specific voice commands. The system has been designed to be user-friendly, and the voice commands are simple and easy to remember. The embedded system will also be quite energy efficient. The system can be attached to the bike using adhesive tape or cable ties, and the microphone and the embedded hardware can be mounted on the bike frame.
