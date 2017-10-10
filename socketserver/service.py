#!/usr/bin/env python

from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST,PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('send data:',self.rfile.readline().decode())
        data = self.rfile.readline().strip()
        self.wfile.write(bytes(data,encoding='utf-8'))
        #self.wfile.write(ctime().encode())
        #print('.....Connected from:',self.client_address,
        #self.wfile.write('[%s]%s'%(ctime().encode(),self.rfile.readline().encode())))


tcpServer = TCP(ADDR,MyRequestHandler)

print('Waiting for connection...')

tcpServer.serve_forever()