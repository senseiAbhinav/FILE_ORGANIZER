# 📁 File Organizer

A simple and efficient Python script to organize files in a directory based on file types (Documents, Images, Videos, Audio, Code, etc.). It moves each file into categorized subfolders and avoids overwriting by renaming duplicates.

---

## 🚀 Features

- ✅ Organizes files by file extension
- ✅ Supports categories like Documents, Images, Videos, Audio, Archives, Code, and more
- ✅ Automatically creates folders if not present
- ✅ Prevents overwriting by appending numbers to duplicate filenames
- ✅ Uses logging (both to file and console)
- ✅ Cross-platform (Windows, macOS, Linux)
- ✅ Defaults to current working directory if no input is given

---

## 📦 File Categories Supported

| Category      | Extensions                                                                 
|---------------|----------------------------------------------------------------------------
| Documents     | `.pdf`, `.docx`, `.doc`, `.txt`, `.pptx`, `.ppt`, `.xlsx`, `.xls`, `.csv` 
| Images        | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`                  
| Videos        | `.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`, `.wmv`                            
| Audio         | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a`                           
| Archives      | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`                                      
| Executables   | `.exe`, `.msi`, `.sh`, `.bat`, `.apk`                                     
| Code          | `.py`, `.java`, `.c`, `.cpp`, `.js`, `.html`, `.css`, `.php`, `.json`, `.xml` 
| Others        | Any file not matching the above types                                     

---

## 🧰 Requirements

- Python 3.6 or higher (no external libraries required)

---

## 🛠️ How to Use

### 🔹 Run from Command Line

```bash
python organizer.py

### 🔹 Press Enter to organize the current directory **Or**, input a full folder path when prompted:

Enter the full path of the directory to organize: C:\Users\...

**## 🔍 What It Does**
Organizes files by type into folders like Documents/, Images/, Videos/, etc.

Skips folders — only moves actual files.

Avoids overwriting by renaming duplicates (e.g., file_1.txt, file_2.txt).

Logs all activity to organizer.log.

## 🛑 Notes
This script does not delete any files.

It is safe to use — original files are preserved even if names conflict.

You can run it repeatedly on any folder to keep it clean and organized.
