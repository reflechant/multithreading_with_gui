#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Trying to create an async app with Tk. Main module
"""

import sys 
import select
import Queue
import threading

#-------------------------------------------------------------------------------

if sys.version.split()[0][0] == '2':
    import Tkinter as tk
elif sys.version.split()[0][0] == '3':
    import tkinter as tk
else:
    print "Невозможно определить установленную версию интерпретатора Python"
    exit()

#-------------------------------------------------------------------------------

def shift_lbl(event):
    a = S2.get()
    a = a[-1] + a[:-1]
    S2.set(a)
   
#def print_fifo(event):
#    if not queue.empty():
#        S.set(queue.get())
 
def read():
 while True:
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline()
        if line:
            queue.put(line)
        else:
            pass
    else:
        pass

def write():
 while True:
    if not queue.empty():
        #if x:
        #    if S.get()
        x = queue.get()
        S.set(x)

#-------------------------------------------------------------------------------

queue = Queue.Queue()
root = tk.Tk()

S = tk.StringVar()
S2 = tk.StringVar()

L = tk.Label(root, textvariable=S, width=50, height=3)
L2 = tk.Label(root, textvariable=S2)
B = tk.Button(root, text = "НАЖМИ МЕНЯ")

L.pack()
L2.pack()
B.pack()

S.set("TEXT")
S2.set("TEXT")

B.bind("<Button-1>", shift_lbl)

#-------------------------------------------------------------------------------

root.mainloop()
thread = threading.Thread(target = read)
thread.start()

thread2 = threading.Thread(target = write)
thread2.start()
