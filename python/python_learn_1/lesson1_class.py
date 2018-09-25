#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()

class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

emp1.age = 7  # 添加一个 'age' 属性
print emp1.age
emp1.age = 8  # 修改 'age' 属性
del emp1.age  # 删除 'age' 属性

if hasattr(emp1,'age'):
    age = getattr(emp1, 'age')    # 返回 'age' 属性的值
    print age
else:
    print "no age attr====="
    setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
    print "emp1 age %d" % emp1.age
    print Employee

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__


 
class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "销毁"
 
pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3) # 打印对象的id
del pt1
del pt2
del pt3
