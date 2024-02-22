import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def export_to_text_file(inputs):
    with open("user_inputs.txt", "w") as file:
        for i, value in enumerate(inputs, start=1):
            file.write(f"Input {i}: {value}\n")

def upload_to_github():
    try:
        subprocess.run(["git", "add", "user_inputs.txt"])
        subprocess.run(["git", "commit", "-m", "Add user inputs"])
        subprocess.run(["git", "push"])
        messagebox.showinfo("Success", "File uploaded to GitHub successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to upload to GitHub: {str(e)}")

def submit_inputs():
    user_inputs = [entry.get() for entry in entry_list]
    export_to_text_file(user_inputs)
    upload_to_github()

# Create tkinter window
window = tk.Tk()
window.title("User Input Program")

# Create entry widgets
entry_list = []
for i in range(5):
    label = tk.Label(window, text=f"Input {i+1}:")
    label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.E)

    entry = tk.Entry(window)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entry_list.append(entry)

# Create submit button
submit_button = tk.Button(window, text="Submit", command=submit_inputs)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the tkinter event loop
window.mainloop()