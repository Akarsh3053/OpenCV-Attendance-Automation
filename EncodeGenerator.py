import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials, storage, db

cred = credentials.Certificate("admin-service-key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iris-attendance-module-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'storageBucket': 'iris-attendance-module.appspot.com'
})

# Importing Student Images

folderPath = 'Images'
faceImages = os.listdir(folderPath)
imgList = []
studentIds = []
for path in faceImages:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

# Encoding Generation


def findEncodings(imageList):
    encodeList = []
    for img in imageList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


encodeListKnown = findEncodings(imgList)
faceEncodings_withId = [encodeListKnown, studentIds]

file = open("FaceEncodings.p", 'wb')
pickle.dump(faceEncodings_withId, file)
file.close()
