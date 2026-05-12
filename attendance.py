from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch


def speak(text):

    speaker = Dispatch("SAPI.SpVoice")

    speaker.Speak(text)
if not os.path.exists("Attendance"):

    os.makedirs("Attendance")


video = cv2.VideoCapture(0)

if not video.isOpened():

    print("Camera Not Working")

    exit()



facedetect = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)


with open('data/names.pkl', 'rb') as w:

    LABELS = pickle.load(w)

with open('data/faces_data.pkl', 'rb') as f:

    FACES = pickle.load(f)


min_len = min(len(LABELS), len(FACES))

LABELS = LABELS[:min_len]

FACES = FACES[:min_len]


knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(FACES, LABELS)

date = datetime.now().strftime("%d-%m-%Y")

filename = f"Attendance/Attendance_{date}.csv"


while True:

    ret, frame = video.read()

    if not ret:

        print("Frame Not Captured")

        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = facedetect.detectMultiScale(
        gray,
        1.3,
        5
    )

    for (x, y, w, h) in faces:

        crop_img = frame[y:y+h, x:x+w]

        resized_img = cv2.resize(
            crop_img,
            (50,50)
        ).flatten().reshape(1,-1)

        output = knn.predict(resized_img)

        distance, index = knn.kneighbors(resized_img)

        
        name = output[0]


        if distance[0][0] > 3000:

            name = "Unknown"


        if name == "Unknown":

            color = (0,0,255)

        else:

            color = (0,255,0)

        
        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            color,
            3
        )

        
        cv2.putText(
            frame,
            str(name),
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,255,255),
            2
        )

        if name != "Unknown":

            time_now = datetime.now().strftime("%H:%M:%S")

            already_marked = False

            if os.path.isfile(filename):

                with open(filename, "r") as csvfile:

                    reader = csv.reader(csvfile)

                    for row in reader:

                        if len(row) > 0 and row[0] == name:

                            already_marked = True

                            break

            if not already_marked:

                file_exists = os.path.isfile(filename)

                with open(filename, "a", newline='') as csvfile:

                    writer = csv.writer(csvfile)

                    if not file_exists:

                        writer.writerow(["NAME", "TIME"])

                    writer.writerow([name, time_now])

                print(f"{name} Attendance Marked")

                speak(f"{name} attendance marked successfully")

                cv2.putText(
                    frame,
                    "Attendance Marked Successfully",
                    (20,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    3
                )

                cv2.imshow(
                    "Attendance System",
                    frame
                )

                cv2.waitKey(3000)

                video.release()

                cv2.destroyAllWindows()

                exit()

            else:

                cv2.putText(
                    frame,
                    "Attendance Already Marked",
                    (20,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,255),
                    3
                )


    cv2.imshow(
        "Attendance System",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord('q'):

        print("Attendance System Closed")

        break

video.release()

cv2.destroyAllWindows()