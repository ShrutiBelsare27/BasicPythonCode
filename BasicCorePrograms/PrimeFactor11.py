
'''
@Author: Shruti
@Date: 2021-12-30
@Last Modified by: Shruti
@Last Modified time: 2022-1-1
@Title : To find prime factor
'''
n=int(input("Enter a number:  "))
i=2
while(n!=1):
    rem= n % i
    if(rem==0):
        n=n/i
        print(i)
    else:
        i=i+1
            
    