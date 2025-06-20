# 📁 File Organizer

A clean and efficient Python script that organizes your files into categorized folders based on their extensions. It supports documents, media, code, archives, executables, and more.

---

## 🚀 Features

- ✅ Organizes files by file extension
- ✅ Categorizes into folders like Documents, Images, Code, etc.
- ✅ Avoids overwriting by renaming duplicates
- ✅ Automatically creates folders if they don’t exist
- ✅ Cross-platform: Works on Windows, macOS, and Linux
- ✅ Logs all actions to both console and `organizer.log`
- ✅ Defaults to current directory if no input is provided

---

## 📦 Supported File Categories

| Category     | File Extensions                                                                 |
|--------------|---------------------------------------------------------------------------------|
| Documents    | `.pdf`, `.docx`, `.doc`, `.txt`, `.pptx`, `.ppt`, `.xlsx`, `.xls`, `.csv`       |
| Images       | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`                        |
| Videos       | `.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`, `.wmv`                                  |
| Audio        | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a`                                 |
| Archives     | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`                                            |
| Executables  | `.exe`, `.msi`, `.sh`, `.bat`, `.apk`                                           |
| Code         | `.py`, `.java`, `.c`, `.cpp`, `.js`, `.html`, `.css`, `.php`, `.json`, `.xml`   |
| Others       | Any file that doesn’t match the above types                                     |

---

## 📚 Libraries Used

This project uses only built-in Python libraries — no external packages required:

- `os` — Interact with the operating system (paths, directories)
- `shutil` — High-level file operations (e.g., move files)
- `logging` — Built-in logging to console and file
- `pathlib` — Modern, object-oriented file system paths

Compatible with Python **3.6+**

---

### 🔍 What It Does

- Organizes files **by type** into folders like `Documents/`, `Images/`, `Videos/`, etc.
- Skips directories — only processes files.
- Handles duplicate file names safely (`file.txt` → `file_1.txt`, `file_2.txt`, etc.).
- Creates a `organizer.log` file with all actions.

---
### 🗃️ organizer.log

![image](https://github.com/user-attachments/assets/9939fff6-cb3f-42b1-9380-f3395862eb6d)

---

## 📂 Example Output Structure

```
Downloads/
├── Documents/
│   └── resume.pdf
├── Images/
│   └── photo.jpg
├── Code/
│   └── script.py
├── Archives/
│   └── old_files.zip
├── Others/
│   └── file.jar
├── organizer.log
└── organizer.py
```

---

## 🔐 Safety

- 🛑 No files are deleted — only moved.
- ✅ Renames conflicting files instead of overwriting.
- 🧠 Ideal for regular cleanup of messy folders.

---

## 💡 Future Enhancements

- 🔄 Make it run recursively (include subfolders)
- 🖥️ Add a GUI using Tkinter or PyQt
- 🕒 Schedule regular cleanups using:
  - Windows Task Scheduler
  - macOS Automator
  - Linux `cron` 
