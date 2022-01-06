
'''
@Author: Shruti
@Date: 2022-1-1
@Last Modified by: Shruti
@Last Modified time: 2022-1-2
@Title : The no. of times heads vs tail and find percentage of head vs tail
'''
import random
chances=0
heads=0
tails=0
coin=int(input("Enter the no. of times you want to flip the coin:  "))

while chances!=coin:

		y=random.randint(0, 1)
	
		if y<0.5:
			tails+=1
			chances+=1
		else:
			heads+=1
			chances+=1

print(y)
headspercent = ((heads / (heads + tails)) * 100)
tailspercent = ((tails / (heads + tails)) * 100)  

print("Heads percent: " + str(headspercent)) 
print("Tails percent: " + str(tailspercent)) 