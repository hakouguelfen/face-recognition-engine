import face_recognition
import cv2
import os
import joblib
import numpy as np


def save_new_face(img, label):
    print("Saving face...")

    # Load the image and extract face encoding
    known_image = face_recognition.load_image_file(img)
    known_encodings = face_recognition.face_encodings(known_image)

    # Check if there are any faces detected
    if not known_encodings:
        print("No faces found in the image.")
        return

    # Take the first face encoding (you can modify this to handle multiple faces)
    known_encoding = known_encodings[0]

    encodings_file = "output/encodings.pkl"

    # Check if the encodings file exists
    if os.path.exists(encodings_file):
        # Load existing encodings
        encodings = joblib.load(encodings_file)
        # Append the new encoding with its label
        encodings.append({"label": label, "encoding": known_encoding})
    else:
        # If the file doesn't exist, create a new list with the encoding
        encodings = [{"label": label, "encoding": known_encoding}]

    # Save the updated encodings list
    joblib.dump(encodings, encodings_file)
    print("Face has been saved.")


def predict_face(img):
    encodings_file = "output/encodings.pkl"

    # Check if encodings file exists
    if not os.path.exists(encodings_file):
        print("No encodings found, please save faces first.")
        return None

    # Load encodings from the file
    encodings = joblib.load(encodings_file)

    # Load and encode the unknown image
    unknown_image = face_recognition.load_image_file(img)
    unknown_encodings = face_recognition.face_encodings(unknown_image)

    # Check if any faces are found in the unknown image
    if not unknown_encodings:
        print("No faces found in the image.")
        return None

    best_match = None

    # Compare the first unknown encoding with the known encodings
    for item in encodings:
        label = item["label"]
        encoding = item["encoding"]

        # Compare faces using face_recognition.compare_faces
        results = face_recognition.compare_faces([encoding], unknown_encodings[0])

        if results[0]:  # If the first encoding matches
            best_match = label
            break  # Break early once a match is found

    if best_match is not None:
        return f"Face recognized as {best_match}"
    else:
        return "Face not recognized"
