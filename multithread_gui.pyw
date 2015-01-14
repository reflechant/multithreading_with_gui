#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Trying to create an async app with Tk. Main module
"""

import sys 
import select
import Queue
import threading
import time

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
 
"""def read(ev_for_wait, ev_for_set):
 while True:
    #if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        ev_for_wait.wait()
        ev_for_wait.clear()
        
        line = sys.stdin.readline()
        if line:
            queue.put(line)
            ev_for_set.set()
        else:
            pass
    #else:
    #    pass
    #time.sleep(0.001)"""

def read():
 while True:
    line = sys.stdin.readline()
    if line:
        S.set(line)
    else:
        break

"""def write(ev_for_wait, ev_for_set):
 while True:
    ev_for_wait.wait()
    ev_for_wait.clear()

    if not queue.empty():
        x = queue.get()
        ev_for_set.set()
        #print(x)
        S.set(x)
        #root.update_idletasks()
        root.update()
    #time.sleep(0.001)"""

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
#ev1 = threading.Event()
#ev2 = threading.Event()

thread = threading.Thread( target = read )
#thread = threading.Thread(target = read, args = (ev1,ev2) )
#thread2 = threading.Thread(target = write, args = (ev2,ev1) )

thread.start()
#thread2.start()

#ev2.set()
#thread.join()
#thread2.join()

root.mainloop()
#thread.join()
