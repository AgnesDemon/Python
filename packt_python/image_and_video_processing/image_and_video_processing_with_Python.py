#We are building an app that detects moving objects from the computer webcam.
#Then the app will store and visualize the time when the objects entered and exited the video frame.
#Computer vision is the field that deals with acquiring and processing images, then makes decisions based on those images.
#Computers can tell you how many phases there are in an image, what color dominates the image, etc.
#We will use Python to load and process images and allow face and motion detection.
#OpenCV - Open Source Computer Vision.

import cv2
import glob
import time
#glob is a library that finds path names of files

'''#img = cv2.imread("galaxy.jpg", 0) #0 makes the image black, gray, and white.
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

#Shows each image for 500 miliseconds (1/2 second), closes each image, and saves them.
'''images = glob.glob("*.jpg") #looks and makes a list of files that end in .jpg.

for image in images:
    img = cv2.imread(image,0) #black and white image due to 0.
    re = cv2.resize(img, (100,100)) #image is resized and saved in a variable.
    cv2.imshow("Hey", re)
    cv2.waitKey(500) #waits 500 miliseconds, or approximately 1/2 a second.
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" + image, re) #renames image to resized_(image name).
    #Example: resized_galaxy.jpg.'''

#Allows you to map out face in an image with a square/rectangle.
'''face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.05, minNeighbors=5)
#scaleFactor = 1.05 will decrease the scale by 5%.
#If you were to put 1.5 in scaleFactor, it would decrease the scale by 50%.

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
    #Draws a square or rectangle that maps out the face.

print(type(faces)) #Prints what class faces is.
print(faces) #Prints the values that define the face in the image.

resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Gray", img) #Shows image.
cv2.waitKey(0)
cv2.destroyAllWindows()

#In cases with images with more than one face or unclear faces, you can adjust the scaleFactor to better find the faces.
#However, it won't be perfect. There will be some faces that the program just won't be able to detect.'''

#Captures the first image in a video, opens the image and shows the numpy array of the image.
'''video = cv2.VideoCapture() #You can put 0 for 1 webcam, 1 for two webcams, etc.
#if you are putting in a video upload, type in the name of the video and make sure it is accessible.

check, frame = video.read()

print(check) #check is a boolean value and should print True in the terminal.
print(frame) #frame is a numpy array and should print out a 3-dimensional array because the video is colored.
#The numpy array that frame prints out is also the first image the video captures.

#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#Switch frame in line 80 with gray and a window will open with a gray version of the first image of the video.
time.sleep(3) #this will wait 3 seconds before releasing the camera.
cv2.imshow("Capturing", frame) #Creates a window that shows the first frame, or the image.

cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()
#Line 68 will turn on and access the camera.
#video.release() will release the camera, or stop accessing it.'''

#To show video:
video = cv2.VideoCapture(0) #Starts video
#If using a video: cv2.VideoCapture("video_name.mp4").
while True:
    check, frame = video.read()
    print(check) #boolean value
    print(frame) #numpy array
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray) #shows you the image
    key = cv2.waitKey(100)
    #If you reduce the number in the waitKey(), the video will look like it's running smoother.
    if key == ord("q"):
        break #When you press q the while loop will stop.
 #Cool fact! If you block the camera and make it dark, the numpy array values will all turn to 0.
video.release()
cv2.destroyAllWindows()


