import io
import os
import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
# Imports the Google Cloud client library
from google.cloud import vision

client = vision.ImageAnnotatorClient()
def removePic() :
    folder = './recorded'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
def detect_infile(path):
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    objects = client.object_localization(
        image=image).localized_object_annotations
    # print(objects)
    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    likelihood_num = (0,1,2,3,4,5)            

    faces_info = {}
    i = 0
    # Face detection
    for face in faces:
        faces_info[i] = {}
        faces_info[i]['anger'] = likelihood_num[face.anger_likelihood]
        faces_info[i]['joy'] = likelihood_num[face.joy_likelihood]
        faces_info[i]['sorrow'] = likelihood_num[face.sorrow_likelihood]
        faces_info[i]['surprise'] = likelihood_num[face.surprise_likelihood]
        all_emotions = {'anger' : likelihood_num[face.anger_likelihood],  'joy' :likelihood_num[face.joy_likelihood], 
        'sorrow' :likelihood_num[face.sorrow_likelihood], 'surprise' :likelihood_num[face.surprise_likelihood]}
        all_emotions = {k: v for k, v in sorted(all_emotions.items(), key=lambda item: item[1], reverse=True)}
        emo_values = all_emotions.values()
        value_iterator = iter(emo_values)
        first_value = next(value_iterator)

        verticesX = ([vertex.x
                    for vertex in face.bounding_poly.vertices])
        verticesY = ([vertex.y
                    for vertex in face.bounding_poly.vertices])
        if first_value == 1 :
            faces_info[i]['current_emo'] = 'default'
        else :
            faces_info[i]['current_emo'] = list(all_emotions.keys())[0]
        
        faces_info[i]['vertices'] = [verticesX[0], verticesY[0],verticesX[2],verticesY[2]]
        i += 1

    objects_dict = {}
    j = 0
    #object detection
    for object_info in objects:
        if object_info.name != "Person" :
            verticesX = ([vertex.x for vertex in object_info.bounding_poly.normalized_vertices])
            verticesY = ([vertex.y for vertex in object_info.bounding_poly.normalized_vertices])

            objects_dict[j] = {"name" : object_info.name, 'vertices' : [int(verticesX[0] * img_width), int(verticesY[0] * img_height),int(verticesX[2] * img_width),int(verticesY[2] * img_height)]}
            j += 1

    return {'face_info' : {'current_emo' : faces_info[0]['current_emo'], 'vertices' : faces_info[0]['vertices'] }, 'objects' : objects_dict}
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
removePic()
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
anterior = 0
count = 0
while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()
    img_width = frame.shape[0]
    img_height = frame.shape[1]
    if ret:
        cv2.imwrite("./recorded/image"+str(count)+".jpg", frame)     # save
        objects_info = detect_infile("./recorded/image"+str(count)+".jpg")
        # print(objects_info)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Draw a rectangle around the faces
        
        vertices = objects_info['face_info']['vertices']
        cv2.rectangle(frame, (vertices[0], vertices[1]), (vertices[2], vertices[3]), (0, 255, 0), 2)
        cv2.putText(frame,objects_info['face_info']['current_emo'], (vertices[0] , vertices[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        for j in objects_info['objects'] :
            object_info = objects_info['objects'][j]

            obj_vertices = object_info['vertices']
            cv2.rectangle(frame, (obj_vertices[0], obj_vertices[1]), (obj_vertices[2], obj_vertices[3]), (0, 255, 0), 2)
            cv2.putText(frame,object_info['name'], (obj_vertices[0] , obj_vertices[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # # Display the resulting frame
    cv2.imshow('Video', frame)
    
    # frame = er.recognise_emotion(frame, return_type='BGR')
    cv2.imshow('Video', frame)
    count += 1
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
removePic()

