import cv2
import face_recognition
import pickle
import os

# Importing Student Images

folderPath = 'Images'
faceImages = os.listdir(folderPath)
imgList = []
studentIds = []
for path in faceImages:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

# Encoding Generation


def findEncodings(imageList):
    encodeList = []
    for img in imageList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)


encodeListKnown = findEncodings(imgList)

file = open("FaceEncodings.p", 'wb')
pickle.dump(encodeListKnown, file)
file.close()


