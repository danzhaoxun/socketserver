#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)


while True:
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('>>>')
    if not data:
        break;
    tcpCliSock.sendall(('%s\r\n'%data).encode())
    date = tcpCliSock.recv(BUFSIZ)
    if not date:
        break;
    print(date.strip().decode())
    tcpCliSock.close()