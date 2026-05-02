
import time, face_recognition, os, cv2
from . import encodingLoader
def detectFaces(windowframe = None,location = None): 
        if location is None or windowframe is None:
                return False 
        # If face locations are found, we call the compareFaces function to compare the detected faces with known encodings. 
        for faces in location:
            #position each corner of the face in the image
            top, right, bottom, left = faces
            # crop the face from the image and display it
            face  = windowframe[top:bottom, left:right]
            cv2.imwrite(os.path.join(encodingLoader.faceDataFolder, "face_{}.jpg".format(time.strftime("%Y-%m-%d_%H-%M-%S"))), face)
            currentEncoding = face_recognition.face_encodings(windowframe,location)
            if len(currentEncoding) == 0:
                return "No face Found"
            currentEncoding = currentEncoding[0]
            matches =  face_recognition.compare_faces(encodingLoader.encodingList,currentEncoding)
            if True in matches:
                firstMatchIndex = matches.index(True)
                return encodingLoader.encodingsName[firstMatchIndex]   