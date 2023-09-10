import cv2 as cv
import face_recognition
import numpy as np
import os
from datetime import datetime, date

path = 'Training_Images'
images = []
classNames = []
img_list = os.listdir(path)


for cl in img_list:
    curImg = cv.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def encoder(images):

    encodelist = []
    for img in images:
        img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

def markAttendance(name):
    file = 'Attendance_Data/'+str(date.today())+'.csv'
    with open(file, 'a+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')


processed_faces = encoder(images)
print('Face Data from images Processed Successfully!!!')

cap = cv.VideoCapture(0)

while True:
    success,img = cap.read()
    imgS = cv.resize(img,(0,0),None,0.25,0.25)
    imgS = cv.cvtColor(imgS, cv.COLOR_BGR2RGB)

    face_count = face_recognition.face_locations(imgS)
    frame_encode = face_recognition.face_encodings(imgS,face_count)

    for encodeFace,faceLoc in zip(frame_encode,face_count):
        matches = face_recognition.compare_faces(processed_faces,encodeFace)
        face_distance = face_recognition.face_distance(processed_faces,encodeFace)
        match_index = np.argmin(face_distance)

        if matches[match_index]:
            name = classNames[match_index].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv.FILLED)
            cv.putText(img, name, (x1 + 6, y2 - 6), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)
        else:
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv.FILLED)
            cv.putText(img, "Unknown", (x1 + 6, y2 - 6), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cv.imshow('Webcam',img)
    cv.waitKey(1)




