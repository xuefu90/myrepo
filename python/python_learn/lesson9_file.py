#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开一个文件
fo = open("foo.txt", "w")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
fo.close()

fo = open("foo.txt","a+")
fo.write('hello world!!!\n')
position = fo.tell()
print "当前文件位置1 : ", position
fo.close()

fo = open('foo.txt','a+')
position = fo.tell()
print "当前文件位置2 : ", position
fo.write('good!!!\n')
# 查找当前位置
position = fo.tell()
print "当前文件位置3 : ", position
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read()
print str

import os
print dir(os)
os.rename("foo.txt","test.txt")

os.remove("test.txt")



