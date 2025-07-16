import os
import shutil

target_directory = os.path.join(os.path.expanduser("~"), "Downloads")

file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"]
}

def organize_file():
    if not os.path.exists(target_directory):
        return "Target folder not found"
   
    files_moved = 0

    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()

            for category, extensions in file_categories.items():
                if ext in extensions:
                    category_folder = os.path.join(target_directory, category)
                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    files_moved += 1
                    break

    return f"Organized {files_moved} files." if files_moved else "No files needed organizing."