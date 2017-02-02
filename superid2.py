#!/usr/bin/env python

from __future__ import print_function

# Libraries we need
import pyxhook
import time
import subprocess
import re

nounlist = open("nounlist.txt","r")

stringtosearch = ""


# This function is called every time a key is presssed
def kbevent(event):
    global running
    global stringtosearch
    # print key info
    #print(event)
    #stringtosearch += chr(event.Ascii)
#    print (stringtosearch)
    # If the ascii value matches spacebar, terminate the while loop
    if event.Ascii == 32:
        #print (stringtosearch)
	query = r"\b" + stringtosearch + r"\b"
	if re.search(query, open("nounlist.txt","r").read(), re.IGNORECASE): 
#        p=subprocess.Popen(["firefox","www." + stringtosearch + ".com"])
		print ("http://www.wikipedia.org/wiki/" + stringtosearch)
		print ("http://www.google.com/#?=" + stringtosearch)
		#subprocess.Popen(["firefox", "www.wikipedia.org/wiki/"+ stringtosearch])
	stringtosearch = ''
    elif event.Ascii == 27:
        #print (stringtosearch)
        running = False
    else:
        stringtosearch += chr(event.Ascii)
	#print (stringtosearch)

# Create hookmanager
hookman = pyxhook.HookManager()
# Define our callback to fire when a key is pressed down
hookman.KeyDown = kbevent
# Hook the keyboard
hookman.HookKeyboard()
# Start our listener
hookman.start()

# Create a loop to keep the application running
running = True
while running:
    time.sleep(0.1)

# Close the listener when we are done
hookman.cancel()


