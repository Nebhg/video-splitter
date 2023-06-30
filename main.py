# Importing all necessary libraries
from random import random

import cv2
import os
import shutil

# Read the video from specified path
fileName = input("Please enter the name of your file: ")
cam = cv2.VideoCapture("C:/Users/benha/Desktop/clips/" + fileName + ".mp4")

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while True:

    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'  
        print('Creating...' + name)
        old_name = ""
        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1

    else:
        break

image_list = sorted(os.listdir('C:/Users/benha/Desktop/pythonProject/data'))






# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()


