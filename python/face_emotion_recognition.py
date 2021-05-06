from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import face_recognition
import keras
from keras.models import load_model
import cv2


face_locations = face_recognition.face_locations(image)
emotion_dict= {'Angry': 0, 'Sad': 5, 'Neutral': 4, 'Disgust': 1, 'Surprise': 6, 'Fear': 2, 'Happy': 3}

video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
anterior = 0
model_emotions = load_model("model_v6_23.hdf5")
while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_emotion = np.reshape(gray, [1, gray.shape[0], gray.shape[1], 1])
    predicted_class = np.argmax(model.predict(face_emotion))
    
    label_map = dict((v,k) for k,v in emotion_dict.items()) 
    predicted_label = label_map[predicted_class]
    print(predicted_label)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame,predicted_label, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))


    # Display the resulting frame
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
