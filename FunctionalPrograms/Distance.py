'''
@Author: Shruti
@Date: 2022-1-2
@Last Modified by: Shruti
@Last Modified time: 2022-1-2
@Title :To calculate distance  use math.power function
'''
import math
import sys
print(sys.argv)
X = int(sys.argv[1])
Y = int(sys.argv[2])

distance = math.sqrt(X * X + Y * Y ) #Use Math.power function
print(distance)