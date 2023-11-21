import cv2
import os
import pickle

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

# Loading mode graphics for attendance system
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))


# Load Encodings
file = open('FaceEncodings.p', 'rb')
faceEncodings_withId = pickle.load(file)
encodeListKnown, studentIds = faceEncodings_withId



while True:
    success, img = cap.read()

    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[2]

    cv2.imshow("IRIS: Attendance Module", imgBackground)
    cv2.waitKey(1)