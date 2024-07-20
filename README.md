# File Organizer

## Description

A simple Python application to organize files in a directory based on their extension.
The script moves files into folders named after their types (e.g., Images, Documents, Music, etc.).

## Requirements 

- Python 3.12.2
- 'os' and 'shutil' modules

## Usage

1. Clone the repository: 
2. Open a terminal and navigate to the project directory.
3. Run the script:
    ```bash
    python main.py
    ```
4. Enter the path of the directory you want to organize. (Just copy the file path into the terminal)

## Example

Suppose you have a directory with the following files:
    - image.jpg
    - document.pdf
    - song.mp3


After running the script, the directory will be organized as follows:
    directory/
    |--Images/
    |`--image.jpg
    |-- Documents/
    |`--document.pdf 
    |-- Music/
    |`--song.mp3