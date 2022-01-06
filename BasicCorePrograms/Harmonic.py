'''
@Author: Shruti
@Date: 2021-12-30
@Last Modified by: Shruti
@Last Modified time: 2022-1-4
@Title : Print the harmonic value
'''

sum=0
num=int(input("Enter a number "))
if num>=1:
    i=num
    for i in range(1,num+1):
        #sum=sum+(1/i) # harmonic sum calculation
        sum =sum+ (1) / i;
        print("value of 1/",i ," is ",  1/i)


            
    print("Harmonic sum is",sum) 
    
else:
    print("Number should not equal to zero and less than zero")