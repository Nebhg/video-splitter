# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture("C:/Users/benha/Desktop/bball/post fade.mp4")

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while (True):

    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1

    else:
        break

image_list = sorted(os.listdir('C:/Users/benha/Desktop/pythonProject/data'))

for i, img in enumerate(image_list):
    if i % 3 != 0:
        img_path = os.path.join('C:/Users/benha/Desktop/pythonProject/data', img)
        os.remove(img_path)
print('Deleting...' + str(i/3) + 'images')
# Release all space and windows once done
cam.release()

cv2.destroyAllWindows()
