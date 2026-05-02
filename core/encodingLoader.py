import os, face_recognition
# This module is responsible for loading the known face encodings and their corresponding names from the specified directories.
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
faceDataFolder = os.path.join(BASE_DIR, "data", "faceData")
encodingDirectory = os.path.join(BASE_DIR, "data", "encodings")
fileHolder = str(None)
encodingList = []
encodingsName = []
# Ensure that the directories for storing face data and encodings exist. 
# If they do not exist, they are created using os.makedirs().
if not os.path.exists(faceDataFolder):
    os.makedirs(faceDataFolder)
if not os.path.exists(encodingDirectory):
    os.makedirs(encodingDirectory)
# Walk through the encoding directory and load the known face encodings and their corresponding names into separate lists. 
# The face encodings are extracted from the images in the encoding directory using the face_recognition library, 
# and the names are derived from the directory structure.
for root, dirs, files in os.walk(encodingDirectory):
        for file in files:
            fileHolder = os.path.join(root, file)
            knownEncodings = face_recognition.face_encodings(face_recognition.load_image_file(fileHolder)) 
            if len(knownEncodings)>0:
                encodingList.append(knownEncodings[0])
            name = os.path.basename(root)
            encodingsName.append(name)
print(f"Loaded {len(encodingList)} encodings")
