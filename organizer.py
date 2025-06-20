import os
import shutil
import logging
from pathlib import Path

# --- Setup Logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("organizer.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# --- File Type Categories ---
FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".ppt", ".xlsx", ".xls", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".sh", ".bat", ".apk"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".php", ".json", ".xml"],
    "Others": []
}

# --- Determine File Category Based on Extension ---
def get_category(extension: str) -> str:
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

# --- Safely Move File without Overwriting ---
def move_file_safely(src_path: Path, dest_folder: Path):
    dest_folder.mkdir(parents=True, exist_ok=True)
    dest_path = dest_folder / src_path.name

    count = 1
    while dest_path.exists():
        new_name = f"{src_path.stem}_{count}{src_path.suffix}"
        dest_path = dest_folder / new_name
        count += 1

    shutil.move(str(src_path), str(dest_path))
    logging.info(f"Moved '{src_path.name}' to '{dest_folder.name}/'")
    return dest_path

# --- Main Organizer Function ---
def organize_files(target_dir: str):
    target = Path(target_dir).resolve()

    if not target.is_dir():
        logging.error(f"Invalid directory: {target}")
        print("❌ Invalid directory path.")
        return

    files_moved = 0

    for item in target.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            category_folder = target / category

            try:
                move_file_safely(item, category_folder)
                files_moved += 1
            except Exception as e:
                logging.error(f"Failed to move '{item.name}': {e}")
        else:
            logging.debug(f"Skipped directory: {item.name}")

    print(f"✅ File organization complete. {files_moved} file(s) organized.")
    logging.info(f"Organization complete. {files_moved} file(s) organized in '{target}'.")

# --- Script Entry Point ---
if __name__ == "__main__":
    print("📁 File Organizer Script")
    user_input = input("Enter the full path of the directory to organize (leave blank for current directory): ").strip()
    directory_to_organize = user_input if user_input else os.getcwd()
    organize_files(directory_to_organize)
