#We are building an app that detects moving objects from the computer webcam.
#Then the app will store and visualize the time when the objects entered and exited the video frame.
#Computer vision is the field that deals with acquiring and processing images, then makes decisions based on those images.
#Computers can tell you how many phases there are in an image, what color dominates the image, etc.
#We will use Python to load and process images and allow face and motion detection.
#OpenCV - Open Source Computer Vision.

import cv2
import glob
#glob is a library that finds path names of files

'''#img = cv2.imread("galaxy.jpg", 0)
#img = cv2.imread("galaxyjpg", 1)
img = cv2.imread("galaxy.jpg", -1)

print(type(img)) #shows the class of the image.
print(img) #I believe this shows the actual image. If not, it may be line 20.
print(img.shape) #gives a tuple with the dimensions of the image.
print(img.ndim) #gives the number of dimensions in an image.

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2))) #reduces the image size by half, then rounds to the nearest integer.
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0) #0 will allow you to press any button to close the image.
#If you type another number, that will be the amount of miliseconds the image will last before closing on its own.
cv2.destroyAllWindows()'''

images = glob.glob("*.jpg") #looks and makes a list of files that end in .jpg.

for image in images:
    img = cv2.imread(image,0) #black and white image due to 0.
    re = cv2.resize(img, (100,100)) #image is resized and saved in a variable.
    cv2.imshow("Hey", re)
    cv2.waitKey(500) #waits 500 miliseconds, or approximately 1/2 a second.
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" + image, re) #renames image to resized_(image name).

