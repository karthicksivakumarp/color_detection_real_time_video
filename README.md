# color_detection_real_time_video
Color Detection (Red, Yellow, Green, Blue, or Unknown) in Real-Time Video using OpenCV
This Python script utilizes the OpenCV library to perform real-time color detection in a video stream from the default camera. 
The goal is to identify and display the dominant color in the captured frames, considering predefined color ranges.

Components:
Function: get_color_name(hue)

Purpose: Determines the color name based on the hue value.
Input: Hue value.
Output: Color name (Red, Yellow, Green, Blue, or Unknown).
Video Capture Initialization:

Opens the default camera using cv2.VideoCapture(0).
Main Loop (Real-Time Video Processing):

Continuously reads frames from the video capture.
Converts each frame to the HSV (Hue, Saturation, Value) color space using cv2.cvtColor.
Defines color ranges for Red, Yellow, Green, and Blue.
Color Detection Algorithm:

For each color range, a mask is created using cv2.inRange to isolate pixels within the specified color range.
The average hue value is calculated in the region covered by the mask using np.mean.
The detected color is determined by comparing the average hue to the predefined color ranges.
Display:

The detected color is displayed on the video frame using cv2.putText.
The processed frame is shown in a window named 'frame' using cv2.imshow.
Termination:

The script exits the loop and releases the video capture when the 'q' key is pressed.
Usage:
Run the script, and a window will appear showing the real-time video feed with the detected dominant color displayed on each frame.
Press the 'q' key to close the window and terminate the script.
Note:
The script uses predefined color ranges for Red, Yellow, Green, and Blue. Adjustments to these ranges may be necessary based on lighting conditions and specific color variations in the environment.
This script provides a simple demonstration of real-time color detection in a video stream and serves as a starting point for more sophisticated color recognition applications. Adjustments and enhancements can be made to improve accuracy and performance based on specific use cases.
