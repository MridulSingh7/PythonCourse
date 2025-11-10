import os
import shutil
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

WATCH_FOLDER = os.path.expanduser("~/Downloads") #gives full path

FILE_DESTS = {
    '.pdf': 'PDFs',
    '.jpg': 'JPGs',
    '.jpeg': 'JPGs',
    '.png': 'Images',
}

class FileMoverHandler(FileSystemEventHandler): #creating subclass such that this function only happens for some specific events (like being created)
    def on_created(self, event):
        if event.is_directory: 
            return
        
        time.sleep(1)
        file_path = event.src_path #full path of the event 
        ext = os.path.splitext(file_path)[1].lower() 
        dest_folder = FILE_DESTS.get(ext, 'Others') #mapping in the dictionary
        full_dest = os.path.join(WATCH_FOLDER, dest_folder)  
        os.makedirs(full_dest, exist_ok=True)

        move_to = os.path.join(full_dest, os.path.basename(file_path))#This returns just the file’s name, without any folder path.

        if os.path.exists(move_to):
            base, extn = os.path.splitext(move_to)
            count = 1
            while os.path.exists(move_to):
                move_to = f"{base}_{count}{extn}"
                count += 1

        try:
            shutil.move(file_path, move_to)
            print(f"Moved: {os.path.basename(file_path)} → {dest_folder}")
        except Exception as e:
            print(f"Failed to move {file_path}: {e}")

if __name__ == "__main__":
    print(f"Watching folder: {WATCH_FOLDER}")
    event_handler = FileMoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped watching.")
        observer.stop()
    observer.join()
