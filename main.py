import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

# Global Variables
original_image = None
encrypted_image = None
decrypted_image = None
key = 123  # XOR key

def load_image():
    global original_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        original_image = Image.open(file_path).convert("RGB")
        display_image(original_image, original_label, "Original Image Loaded")

def save_image(img, filename):
    if img:
        img.save(filename)
        messagebox.showinfo("Saved", f"Image saved as {filename}")
    else:
        messagebox.showerror("Error", "No image to save!")

def encrypt():
    global encrypted_image
    if original_image:
        data = np.array(original_image)
        encrypted_data = data ^ key
        encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
        display_image(encrypted_image, encrypted_label, "Encrypted")
    else:
        messagebox.showerror("Error", "Load an image first.")

def decrypt():
    global decrypted_image
    if encrypted_image:
        data = np.array(encrypted_image)
        decrypted_data = data ^ key
        decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
        display_image(decrypted_image, decrypted_label, "Decrypted")
    else:
        messagebox.showerror("Error", "Encrypt an image first.")

def display_image(img, label, text):
    img_resized = img.resize((200, 200))
    tk_img = ImageTk.PhotoImage(img_resized)
    label.config(image=tk_img)
    label.image = tk_img
    label_text.config(text=text)

# GUI Setup
app = tk.Tk()
app.title("Image Encryption Tool")
app.geometry("700x500")
app.configure(bg="#F0F0F0")

tk.Label(app, text="Pixel Manipulation for Image Encryption", font=("Helvetica", 16, "bold")).pack(pady=10)

btn_frame = tk.Frame(app)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Load Image", command=load_image, width=15).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Encrypt", command=encrypt, width=15).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Decrypt", command=decrypt, width=15).grid(row=0, column=2, padx=10)

save_frame = tk.Frame(app)
save_frame.pack(pady=10)

tk.Button(save_frame, text="Save Encrypted", command=lambda: save_image(encrypted_image, "encrypted_image.png"), width=15).grid(row=0, column=0, padx=10)
tk.Button(save_frame, text="Save Decrypted", command=lambda: save_image(decrypted_image, "decrypted_image.png"), width=15).grid(row=0, column=1, padx=10)

img_frame = tk.Frame(app)
img_frame.pack(pady=20)

original_label = tk.Label(img_frame)
original_label.grid(row=0, column=0, padx=10)

encrypted_label = tk.Label(img_frame)
encrypted_label.grid(row=0, column=1, padx=10)

decrypted_label = tk.Label(img_frame)
decrypted_label.grid(row=0, column=2, padx=10)

label_text = tk.Label(app, text="", font=("Helvetica", 12))
label_text.pack()

app.mainloop()
