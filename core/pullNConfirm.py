import cv2 , numpy as np ,face_recognition
from mss import mss
from . import detection
def pullVideo():
        # Define the bounding box for the screen capture. The bounding box is defined by its top-left corner (top, left) and its width and height. 
        bounding_box = {'top': 200, 'left': 0, 'width': 900, 'height': 800}
        sct = mss()
        #fc = 0
        #fs = 25
        while True:
            # Capture the screen within the defined bounding box and convert it to a format suitable for face recognition. 
            # The captured screen is converted from BGR color space (used by OpenCV) to RGB color space (used by face_recognition) to ensure compatibility with the face recognition library. 
            windowFrame = cv2.cvtColor(np.array(sct.grab(bounding_box)), cv2.COLOR_BGR2RGB)
            #if fc % fs == 0:
            face_locations = face_recognition.face_locations(windowFrame)     
            #fc += 1
            # If face locations are found, we call the compareFaces function to compare the detected faces with known encodings. The results of the comparison are printed for debugging purposes. 
            # This allows us to continuously check for new faces in subsequent frames without retaining old face location data.
            if face_locations:
                ## If a face is detected, an email alert is sent using the Mailtrap service. The email contains information about the detected face and the time of detection. 
                # After sending the email, the face location data is cleared to prepare for the next detection cycle.
                print(f"\r Face comparison result: {detection.detectFaces(windowFrame, face_locations)}           ",end=" ",flush=True)
                #uncomment to enable alerting
                # detection.sendAlert(detection.detectFaces(windowFrame, face_locations))
                face_locations = None
            else:
                # If no faces are detected, a message is printed to indicate that no faces were found in the current frame. 
                print(f"\r Face comparison result: No face found           ",end=" ",flush=True)
if __name__ == "__main__":
    pullVideo()
