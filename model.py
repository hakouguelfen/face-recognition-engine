import face_recognition
import os
import joblib


def save_new_face(img, label):
    known_image = face_recognition.load_image_file(img)
    known_encodings = face_recognition.face_encodings(known_image)

    if not known_encodings:
        return

    known_encoding = known_encodings[0]

    encodings_file = "output/encodings.pkl"

    if os.path.exists(encodings_file):
        encodings = joblib.load(encodings_file)
        encodings.append({"label": label, "encoding": known_encoding})
    else:
        encodings = [{"label": label, "encoding": known_encoding}]

    joblib.dump(encodings, encodings_file)


def predict_face(img):
    encodings_file = "output/encodings.pkl"

    if not os.path.exists(encodings_file):
        return None

    encodings = joblib.load(encodings_file)

    unknown_image = face_recognition.load_image_file(img)
    unknown_encodings = face_recognition.face_encodings(unknown_image)

    if not unknown_encodings:
        return None

    best_match = None

    for item in encodings:
        label = item["label"]
        encoding = item["encoding"]

        results = face_recognition.compare_faces([encoding], unknown_encodings[0])

        if results[0]:
            best_match = label
            break

    if best_match is not None:
        return f"Face recognized as {best_match}"
    else:
        return "Face not recognized"
