#!/usr/bin/python
# -*- coding: UTF-8 -*-

for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前水果 :', fruit
 
fruits = ['banana', 'apple',  'mango']
print range(len(fruits))
for index in range(len(fruits)):
   print '当前水果 :', fruits[index]

print range(2,10)
for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j=num/i
            print "%d 等于 %d * %d " %(num,i,j)
            break
    else:
        print num,'是质数'

a=10.0
b=int(a)
print a,int(a),hex(b),oct(b)