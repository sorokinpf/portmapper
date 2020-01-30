#port mapper

#usage
#python portmapper.py listenaddr listenport remoteaddr remoteport

import socket
import sys
import threading

i = 0

def listen(skt_read,skt_write):
  global i
  print ('connected!')
  i+=1
  while True:
    buf = skt_read.recv(1024)
    if buf == '':
      break
    skt_write.send(buf)
  print ('terminated!')
  i-=1

def usage():
  print ('#python portmapper.py listenaddr listenport remoteaddr remoteport')

argv = sys.argv
if len(sys.argv)<5:
  usage()
  exit(-1)

skt = socket.socket()
skt.bind((argv[1],int(argv[2])))
skt.listen(5)

while True:
  try:
    conn,address = skt.accept()
    print (i)
    new_skt = socket.socket()
    new_skt.connect((argv[3],int(argv[4])))
    thread1 = threading.Thread(target=listen,args=(conn,new_skt))
    thread2 = threading.Thread(target=listen,args=(new_skt,conn))
    thread1.start()
    thread2.start()
  except KeyboardInterrupt:
    skt.close()
    exit(-1)
