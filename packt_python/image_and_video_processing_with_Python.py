#We are building an app that detects moving objects from the computer webcam.
#Then the app will store and visualize the time when the objects entered and exited the video frame.
#Computer vision is the field that deals with acquiring and processing images, then makes decisions based on those images.
#Computers can tell you how many phases there are in an image, what color dominates the image, etc.
#We will use Python to load and process images and allow face and motion detection.
#OpenCV - Open Source Computer Vision.

import cv2

img = cv2.imread("galaxy.jpg", 0)
img = cv2.imread("galaxyjpg", 1)
img = cv2.imread("galaxy.jpg", -1)

print(type(img))
print(img)
print(img.shape) #gives a tuple with the dimensions of the image.
print(img.ndim)

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0) #0 will allow you to press any button to close the image.
#If you type another number, that will be the amount of miliseconds the image will last before closing on its own.
cv2.destroyAllWindows()


