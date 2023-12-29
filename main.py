import cv2
import numpy as np


def get_color_name(hue):
    # Define hue ranges for each color
    color_range = {
        "Red": (0, 15),
        "Yellow": (15, 45),
        "Green": (45, 90),
        "Blue": (90, 150),
    }
    # Check which color range the hue falls into
    for color_in, (lower_limit_in, upper_limit_in) in color_range.items():
        if lower_limit_in <= hue <= upper_limit_in:
            return color_in
    return "Unknown"


# Open video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Convert the frame to the HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color ranges for each color
    color_ranges = {
        "Red": ((0, 100, 100), (15, 255, 255)),
        "Yellow": ((15, 100, 100), (45, 255, 255)),
        "Green": ((45, 100, 100), (90, 255, 255)),
        "Blue": ((90, 100, 100), (150, 255, 255)),
    }

    detected_color = "Unknown"

    # Iterate over each color range
    for color, (lower_limit, upper_limit) in color_ranges.items():
        # Create a mask for the current color range
        mask = cv2.inRange(hsv_frame, np.array(lower_limit), np.array(upper_limit))

        # Calculate the average hue in the region
        avg_hue = np.mean(hsv_frame[:, :, 0][mask > 0])

        # Check if the average hue falls into the current color range
        if lower_limit[0] <= avg_hue <= upper_limit[0]:
            detected_color = color
            break

    # Display the detected color on the frame
    cv2.putText(frame, detected_color, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # Show the frame in a window named 'frame'
    cv2.imshow('frame', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
