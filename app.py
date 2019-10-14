from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

destination = ""
source = ""

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
    