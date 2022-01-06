'''
@Author: Shruti
@Date: 2022-1-4
@Last Modified by: shruti
@Last Modified time: 2022-1-4
@Title : To generate distinct coupon number
'''
import random
def coupon(num):
    number="0123456789"
    code= " "
    for i in range(0,num):
        start=random.randint(0,9)
        print(start)
        code=code+number[start:start+1]  #code increment and sliceoperator
    return code
num=int(input("Enter digit:  "))
print(coupon(num))