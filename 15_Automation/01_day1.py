"""
=============================
📘 FILE SORTER EXPLANATION GUIDE
=============================

🧭 Purpose:
This Python script automatically organizes files in a given folder
into categorized subfolders (like “Images”, “PDFs”, “Videos”, etc.)
based on file extensions.

---------------------------------------------------------------
💡 HOW IT WORKS (Step-by-Step)
---------------------------------------------------------------

1️⃣ os.listdir(folder_path)
    - Lists all files and folders inside the given directory.
    Example:
        ["photo.jpg", "movie.mp4", "report.pdf", "notes.txt", "random.xyz"]

2️⃣ full_path = os.path.join(folder_path, file)
    - Creates a full path to the file.
    Example:
        folder_path = "C:\\Users\\Mridul\\Downloads"
        file = "photo.jpg"
        full_path = "C:\\Users\\Mridul\\Downloads\\photo.jpg"

3️⃣ if os.path.isfile(full_path):
    - Ensures the current item is a file (not a folder).
    - Only processes files.

4️⃣ dest_folder = get_destination_folder(file)
    - Determines which folder the file belongs to based on its extension.
    Example mapping:
        EXTENSION_MAP = {
            "PDFs": [".pdf"],
            "Images": [".jpg", ".jpeg", ".png"],
            "Videos": [".mkv", ".mp4", ".mov"],
            "Textfiles": [".txt"]
        }
    Example results:
        "photo.jpg"   -> "Images"
        "movie.mp4"   -> "Videos"
        "report.pdf"  -> "PDFs"
        "notes.txt"   -> "Textfiles"
        "random.xyz"  -> "Others"

5️⃣ dest_path = os.path.join(folder_path, dest_folder)
    - Builds the path for the destination folder.
    Example:
        "C:\\Users\\Mridul\\Downloads\\Images"

6️⃣ shutil.move(full_path, os.path.join(dest_path, file))
    - Moves the file from the original location to the destination folder.

✅ Final folder structure:
    Downloads/
    ├── Images/photo.jpg
    ├── Videos/movie.mp4
    ├── PDFs/report.pdf
    ├── Textfiles/notes.txt
    └── Others/random.xyz

---------------------------------------------------------------
🧰 Debug Tip:
To visualize what’s happening in each iteration:
    print(f"File: {file}")
    print(f"  Full Path: {full_path}")
    print(f"  Destination Folder: {dest_folder}")
    print(f"  Destination Path: {dest_path}\n")

---------------------------------------------------------------
🧠 Key Concepts Used:
    - os.listdir() → list all files
    - os.path.join() → safely join paths
    - os.path.isfile() → check if item is a file
    - os.path.splitext() → get file extension
    - shutil.move() → move files
    - dict iteration (.items()) → map file types to folders
"""

import os
import shutil

EXTENSION_MAP = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mkv", ".mp4", ".mov"],
    "Textfiles": [".txt"]
}

def get_destination_folder(filename):
    file_ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in EXTENSION_MAP.items():
        if file_ext in extensions:
            return folder
    return "Others"

def sort_folders(folder_path):
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            dest_folder = get_destination_folder(file)
            dest_path = os.path.join(folder_path, dest_folder)
            os.makedirs(dest_path, exist_ok=True)

            shutil.move(full_path, os.path.join(dest_path, file))
            print(f"Moved {file} -> {dest_folder}/")

if __name__ == "__main__":
    folder = input("Enter the folder path or leave blank: ").strip()
    folder = folder or os.getcwd()

    if not os.path.isdir(folder):
        print("Invalid directory")
    else:
        sort_folders(folder)
        print("Sorting completed ✅")
