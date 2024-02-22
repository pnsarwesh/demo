import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import os
	
def browse_file():
    file_path = filedialog.askopenfilename()
    print("Selected File:", file_path)
    upload_to_github()
	
def upload_to_github():
    #repo_path = "https://github.com/pnsarwesh/demo"
    #text_file_path = "D:\demo_git\demo\demo1351.txt"
    os.chdir("D:\demo_git\demo")
    subprocess.run(["git", "add", "."])
    subprocess.run(["git","commit", "-m", "Recent Commit"])
    subprocess.run(["git","push"])
    label_result.config(text="Data updated to GitHub repository")
    

# Create the main window
root = tk.Tk()
root.title("GitHub File Uploader")
root.geometry("400x500")

# Create a button to open the file dialog
button = tk.Button(root, text="Select and Upload File", command=browse_file)
button.pack(pady=20)

# Result Label
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
