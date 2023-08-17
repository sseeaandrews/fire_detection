# Fire Detection

This project runs a version of resnet 18 trained on images of fire to detect whether the input image is on fire. The base code streams a webcam input it to an output using webRTC

Check out examples of this in data/notOnFire_onFire/test_output_onFire and in data/notOnFire_onFire/test_output_notOnFire

These examples have the labels Class#0 and Class#1

Class#0 Indicates that the program identified this photo as having no fire

Class#1 Indicates that the program identified this photo as having fire

AI is not perfect. If you go through these photos you can see how it can get confused by large amounts of orange light in the photo, even if there is no flame. This model does not have 100% accuracy so use at your own risk.

## The Algorithm

The algorithm uses a custom trained version of resnet 18 that uses images of things on fire and things not on fire. The code uses that custom model on an input image. The default input with the code is to a webcam streaming to /dev/video0. The default output is to a webRTC server on line 9 that may need to be changed. This code relies on webRTC to work currently but it can be modified. 

## Running this project

This project is designed to be run on a jetson nano developer kit using the jetson inference library. It required the jetson inference library and webRTC to work. Make sure your webcam is connected and inputing to /dev/video0. If it is not you may need to change that in the code. Make sure the webRTC port is correct for your nano. 

0. Be connected to your nano: Make sure your nano is connected to internet and that you have succesfully SSHed into your nano.

1. Navigate to the directory the python script fireDetection.py is dowloaded in using the command'cd fire_detection'. 

2. Run the command 'ls' and make sure you see fireDetection.py in the output.

3. Run the command 'python3 fireDetection.py'

4. If your input and output is correct you should be able to see the stream by searching 'http://ubuntu:<your_port_number>/'

If you do not see the stream make sure everything is installed correctly and your inputs and outputs are correct.

[View a video explanation here]
https://www.youtube.com/watch?v=T_XQkzqx7No