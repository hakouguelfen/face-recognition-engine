from flask import Flask, request

import model

app = Flask(__name__)


@app.route("/save_face", methods=["POST"])
def save_face():
    image = request.files["image"]
    label = request.form["label"]

    model.save_new_face(image, label)
    return {"message": "Saved successfully", "label": label}


@app.route("/predict", methods=["POST"])
def predict():
    image = request.files["image"]

    message = model.predict_face(image)
    return {"message": message}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
