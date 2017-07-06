
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   
from watchdog.observers import Observer
from watchdog.events import *
import time
from post_tip import SendEmail

class FileEventHandler(FileSystemEventHandler):

	def __init__(self):
		FileSystemEventHandler.__init__(self)
	
	def on_created(self, event):
		if event.is_directory:
			print("directory created:{0}".format(event.src_path))
		else:
			flag = 1
			#print("file created:{0}".format(event.src_path))
			#print("true ")
			print flag
			if flag == 1:
				print flag
				se=SendEmail()
				se.main()
		
	
if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler,"E:/img",True)
    observer.start()

    try:
        while True:
            time.sleep(10000)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()