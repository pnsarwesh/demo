
import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def save_to_file():
    demo1351 = [entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get()]
    with open("demo1351.txt", "w") as file:
        for user_input in demo1351:
            file.write(user_input + "\n")
    label_result.config(text="Data saved to demo1351.txt")
    upload_to_github()
    
def upload_to_github():
    #repo_path = "https://github.com/pnsarwesh/demo"
    #text_file_path = "D:\demo_git\demo\demo1351.txt"
    os.chdir("D:\demo_git\demo")
    subprocess.run(["git", "add", "."])
    subprocess.run(["git","commit", "-m", "latest Commit"])
    subprocess.run(["git","push"])
    

# GUI setup
root = tk.Tk()
root.title("User Input Program")

label = tk.Label(root, text="Enter your data:")
label.pack(pady=10)

# Entry Widgets
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=10)

labe2 = tk.Label(root, text="Enter your data:")
labe2.pack(pady=10)

entry2 = tk.Entry(root, width=30)
entry2.pack(pady=10)

labe3 = tk.Label(root, text="Enter your data:")
labe3.pack(pady=10)

entry3 = tk.Entry(root, width=30)
entry3.pack(pady=10)

labe4 = tk.Label(root, text="Enter your data:")
labe4.pack(pady=10)

entry4 = tk.Entry(root, width=30)
entry4.pack(pady=10)

labe5 = tk.Label(root, text="Enter your data:")
labe5.pack(pady=10)

entry5 = tk.Entry(root, width=30)
entry5.pack(pady=10)

# Save Button
save_button = tk.Button(root, text="Save to File", command=save_to_file)
save_button.pack(pady=10)

# Result Label
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()