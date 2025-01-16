import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import requests

class PersonImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Person Image Predictor")
        
        self.left_frame = tk.Frame(root, width=200, height=500)
        self.left_frame.pack(side="left", fill="y")

        self.add_user_button = tk.Button(self.left_frame, text="Add User", command=self.add_user)
        self.add_user_button.pack(pady=20)

        self.predict_person_button = tk.Button(self.left_frame, text="Predict Person", command=self.predict_person)
        self.predict_person_button.pack(pady=20)

        self.image_frame = tk.Frame(root, width=800, height=500, bg="gray")
        self.image_frame.pack(side="left", fill="both", expand=True)

        self.image_label = tk.Label(self.image_frame, text="Image Placeholder", bg="gray")
        self.image_label.pack(expand=True)

    def add_user(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"), ("All files", "*.*")])
        if file_path:
            self.display_image(file_path)
            label = tk.simpledialog.askstring("Input", "Enter label for the person:")
            if label:
                with open(file_path, 'rb') as image_file:
                    response = requests.post(
                        "http://127.0.0.1:3000/save_face",
                        files={"image": image_file},
                        data={"label": label}
                    )
                if response.ok:
                    messagebox.showinfo("Success", f"{response.json()['message']}: {response.json()['label']}")
                else:
                    messagebox.showerror("Error", "Failed to save face")


    def predict_person(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"), ("All files", "*.*")])
        if file_path:
            self.display_image(file_path)
            with open(file_path, 'rb') as image_file:
                response = requests.post(
                    "http://127.0.0.1:3000/predict",
                    files={"image": image_file}
                )
            if response.ok:
                prediction = response.json()['message']
                messagebox.showinfo("Prediction", f"Predicted person: {prediction}")
            else:
                messagebox.showerror("Error", "Failed to predict person")


    def display_image(self, path):
        image = Image.open(path)
        
        original_width, original_height = image.size
        target_width, target_height = 800, 500
        ratio = min(target_width / original_width, target_height / original_height)
        new_size = (int(original_width * ratio), int(original_height * ratio))
        
        image = image.resize(new_size, Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        
        self.image_label.config(image=photo, text="")
        self.image_label.image = photo


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x600")
    app = PersonImageApp(root)
    root.mainloop()