import cv2
from datetime import datetime
import pandas
import time

first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns= ["Start", "End"])

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Changes color frame to gray scale.
    gray = cv2.GaussianBlur(gray, (21, 21), 0) #Blurs gray image.
    
    if first_frame is None:
        first_frame = gray #Assigns the numpy array to first_frame
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    #print(thresh_frame)
    #print(cv2.RETR_EXTERNAL)
    #print(cv2.CHAIN_APPROX_SIMPLE)

    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        #If contours found are greater than 10,000, then the status variable changes from 0 to 1, as shown below.
        status = 1
    
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3) #This is for mapping out the face in "Color Frame."
    status_list.append(status)

    status_list = status_list[-2:]

    print("status list: ", status_list)
    if status_list [-1] == 1 and status_list [-2] == 0:
        print("status list is [1,0]")
        times.append(datetime.now())
    if status_list [-1] == 0 and status_list [-2] == 1:
        print("status list is [0,1]")
        times.append(datetime.now())

    cv2.imshow("Gray Frame", gray) #Shows gray scale frame.
    cv2.imshow("Delta Frame", delta_frame) #Shows frame where you appear see-through.
    cv2.imshow("Threshold Frame", thresh_frame) #Shows the frame where the only colors there are black and white.
    #Black indicates no movement.
    #White indicates movement.
    cv2.imshow("Color Frame", frame) #Shows color frame where your face is inside a green box.

    key = cv2.waitKey(1)
    #print(gray)
    #print(delta_frame)
    #These two print the numpy arrays.

    if key == ord('q'): #If you press 'q' (not in the terminal or code), the windows should close.
        if status == 1:
            times.append(datetime.now())
        break

# print("status list", status_list)
# print(times)

#Error occurs here
for i in range(0, len(times), 2):
    print("times", times)
    print(times[i])
    #df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index = True)
    df_new_row = pandas.DataFrame({"Start": times[i], "End": times[i + 1]}, index = [0])
    df = pandas.concat([df, df_new_row], ignore_index = True)
    print("dataframe", df)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()
#BE SURE TO TURN ON LIGHT BEFORE RUNNING, AS AN ERROR WILL OCCUR BECAUSE IT CANNOT DETECT MOVEMENT
