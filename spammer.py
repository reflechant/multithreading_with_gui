#!/usr/bin/python


from time import time, sleep
import sys

n = input()
t1 = time()

s = "TEST TEXT "
for i in range(int(n)):
    print(s)
    sys.stdout.flush()
    s = s[1:]+s[0]
    sleep(1)

t2 = time()
print(t2-t1)
