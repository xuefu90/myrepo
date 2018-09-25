#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

from socket import *              # 导入 socket 模块
HOST = 'localhost'
PORT = 23456
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    data = raw_input('>')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data
tcpCliSock.close()
