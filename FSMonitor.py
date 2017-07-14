# encoding:utf-8
import os
from pyinotify import WatchManager, Notifier,IN_DELETE, IN_CREATE,IN_MODIFY,ProcessEvent
import time
from post_tip import SendEmail


class EventHandler(ProcessEvent):
	
	
	def process_IN_CREATE(self,event):
		print "Create file:%s" % os.path.join(event.path,event.name)
		print "Send Email"
		se=SendEmail()
		se.main()
		print "call sleep 300s"
		time.sleep(300)
		print "sleep end"
	def process_IN_DELETE(self,event):
		print "Delete file:%s" % os.path.join(event.path,event.name)
	def process_IN_MODIFY(self,event):
		print "Modify file:%s" % os.path.join(event.path,event.name)

def FSMonitor(path='.'):
	wm=WatchManager()
	mask = IN_DELETE|IN_MODIFY|IN_CREATE
	notifier = Notifier(wm,EventHandler())
	wm.add_watch(path,mask,auto_add=True,rec=True)
	print 'now starting monitor %s' %(path)
	while True:
		
		try:
			notifier.process_events()
			if notifier.check_events():
				notifier.read_events()
		except KeyboardInterrupt:
			notifier.stop()
			break
if __name__ == '__main__':
	FSMonitor('/mnt/sda2/webcam/')
		
