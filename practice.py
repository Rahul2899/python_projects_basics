#importing required libraries
import pandas as pd
import numpy as np
import pyautogui
import cv2 as cv
import time

# User input: Duration of recording
t = float(input("Hey Rahul, for how long do you want to record the screen in minutes?   "))

# Calculate total recording time
total_time = t  # Input is already in float (minutes), no need for `pd.to_datetime`
end_time = time.time() + 60 * total_time  # Convert minutes to seconds

# Creating resolution
resolution = pyautogui.size()  # Get screen resolution as a tuple (width, height)

# Define codec and video writer
codec = cv.VideoWriter_fourcc(*"XVID")  # Use XVID codec for compatibility
fps = 20.0  # Frames per second
output = cv.VideoWriter("Test1.avi", codec, fps, resolution)  # Corrected parameter order

# Creating a small window
cv.namedWindow("Live", cv.WINDOW_NORMAL)  # Fixed incorrect function name
cv.resizeWindow("Live", 480, 270)  # Fixed incorrect function name

# Creating a loop for recording
while (time.time()  < end_time ):
    img = pyautogui.screenshot()  # Capture a screenshot
    frame = np.array(img)  # Convert screenshot to a NumPy array
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)  # Convert frame to BGR format for OpenCV
    output.write(frame)  # Write frame to the video file

    # Display the live recording in a window
    cv.imshow("Live", frame)

    # Check for 'q' key press to quit
    if cv.waitKey(1) == ord('q'):
        break

# Release resources and close windows
output.release()
cv.destroyAllWindows()
