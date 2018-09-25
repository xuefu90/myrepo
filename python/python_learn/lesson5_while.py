#!/usr/bin/python
# -*- coding: UTF-8 -*-

numbers=[12,27,28,33,11,8,3,2]
even=[]
odd=[]

print len(numbers)
if len(numbers) > 0:
    print "11111"
else:
    print "22222"

count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
print "Good bye!"


var = 1
while var == 1 :  # 该条件永远为true，循环将无限执行下去
   num = raw_input("Enter a number  :")
   print "You entered: ", num
 
print "Good bye!"

while len(numbers) > 0:
    numbers=numbers.pop()
    if numbers%2==0:
        even.append(numbers)
    else:
        odd.append(numbers)
print numbers,even,odd

