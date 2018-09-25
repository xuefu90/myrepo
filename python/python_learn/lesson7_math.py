#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
var = dir(math)
print 'math = ',var
import cmath
var1 = dir(cmath)
print 'cmath = ',var1

print cmath.sqrt(-1),cmath.sqrt(9),cmath.sin(1),cmath.log10(100)

import random
list = [111,'sfdf','aaa',444]
random.shuffle(list)
print list
print random.choice(range(1,100))

# 输出 100 <= number < 1000 间的偶数
print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)

# 输出 100 <= number < 1000 间的其他数
print "randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3)


random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# 生成同一个随机数
random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# 生成同一个随机数
random.seed( 10 )
print "Random number with seed 10 : ", random.random()
print random.random(),random.random(),random.random()
