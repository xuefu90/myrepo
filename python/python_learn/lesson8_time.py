#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
print time.time()
localtime = time.localtime(time.time())
print localtime
print '==========='
print 'dir(time) = ',dir(time)
localtime = time.asctime(time.localtime(time.time()))
print localtime


# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
 
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

import calendar
 
cal = calendar.month(2018, 9)
print "以下输出2018年9月份的日历:"
print cal

t1 = time.clock()
print t1
t2 = time.clock()
print t2-t1
