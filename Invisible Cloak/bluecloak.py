import cv2
import numpy as np

# Define the color range for blue in the HSV color space
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original frame
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the output
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture
cap.release()

# Close all windows
cv2.destroyAllWindows()
