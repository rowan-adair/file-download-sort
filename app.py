from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os, shutil
import json
import time

destination = "C:/Users/rjada/OneDrive/Documents/Python/download-organisation/Test-1"
source = "C:/Users/rjada/OneDrive/Documents/Python/download-organisation/Test-2"



class Handler(FileSystemEventHandler):
    def on_modified(self,event):
        for filename in os.listdir(source):
            origin = source + "/" + filename
            new_destination = destination + "/" + filename
            os.rename(origin, new_destination)

event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, source, recursive=True)
 
try : 
    while True: 
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()

if __name__ == "__main__":
    print(destination)
    print(source)

