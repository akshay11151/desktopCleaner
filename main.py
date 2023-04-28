import os
import shutil
import time

# Define the paths of the folders where files will be moved
DOCUMENTS_PATH = 'C:/Users/YourUsername/Desktop/Documents'
IMAGES_PATH = 'C:/Users/YourUsername/Desktop/Images'
MUSIC_PATH = 'C:/Users/YourUsername/Desktop/Music'
VIDEOS_PATH = 'C:/Users/YourUsername/Desktop/Videos'
ARCHIVES_PATH = 'C:/Users/YourUsername/Desktop/Archives'

# Define a dictionary of file extensions and their respective folder paths
file_extensions = {
    '.docx': DOCUMENTS_PATH,
    '.pdf': DOCUMENTS_PATH,
    '.txt': DOCUMENTS_PATH,
    '.jpg': IMAGES_PATH,
    '.png': IMAGES_PATH,
    '.mp3': MUSIC_PATH,
    '.mp4': VIDEOS_PATH,
    '.zip': ARCHIVES_PATH,
    '.rar': ARCHIVES_PATH,
    '.7z': ARCHIVES_PATH,
}

while True:
    # Iterate over the files on the desktop and move them to their respective folders
    for filename in os.listdir('C:/Users/YourUsername/Desktop'):
        file_extension = os.path.splitext(filename)[1].lower()
        if file_extension in file_extensions:
            source_path = os.path.join('C:/Users/YourUsername/Desktop', filename)
            destination_path = os.path.join(file_extensions[file_extension], filename)
            shutil.move(source_path, destination_path)

    # Sleep for 5 hours before running the script again
    time.sleep(5 * 60 * 60)
