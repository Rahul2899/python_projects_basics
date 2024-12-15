# Importing the important libraries
import pyautogui
import cv2 as cv
import pandas as pd
import numpy as np
import time

t = float(input("Hey Rahul for how long you want to record the screen in minutes?   "))
a = pd.to_datetime(t , format = "%M")
total_time = a.minute
end_time = time.time() + 60 * total_time


# Defining the resolution for the video
resolution = tuple(pyautogui.size())  # Ensures resolution is a tuple (width, height)

# Defining codec and VideoWriter
codec = cv.VideoWriter_fourcc(*"XVID")  # Changed codec to 'XVID' for better compatibility
fps = 20.0

# Defining output
output = cv.VideoWriter("Test1.avi", codec, fps, resolution)  # Changed output format to .avi

# Creating a small window
cv.namedWindow("Live", cv.WINDOW_NORMAL)
cv.resizeWindow("Live", 480, 270)

# Creating a loop to capture images continuously and merge into a video
while (time.time()  < end_time ):
    img = pyautogui.screenshot()

    frame = np.array(img)
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)  # Converting to BGR format for OpenCV compatibility

    output.write(frame)

    cv.imshow("Live", frame)

    if cv.waitKey(1) == ord('q'):  # Exit loop if 'q' is pressed
        break

output.release()
cv.destroyAllWindows()
