'''
@Author: Shruti
@Date: 2022-1-4
@Last Modified by: shruti
@Last Modified time: 2022-1-5
@Title : To Print Number of Wins and Percentage of Win and Loss.
'''

import random
stake = int(input("Enter stake amount: "))
if stake>0:
    goal = int(input("Enter Goal to be reached: "))
    win = 0
    loss = 0
    totalGambles = 0
   
    
    while stake != 0 and stake != goal:
        gamble = random.randint(0, 2)  
        totalGambles += 1  # Checking the Count of Gambling
        
        if gamble == 0:  # Checking the Gambling number
            stake += 1
            win += 1
        else: 
            stake -= 1
            
            loss += 1
        if stake<=0 and stake>=goal:
            break
    print(" You won ", win, " times ")
    print(" You Lost ", loss, " times ")
    print(" Your Total Gamble Played ", totalGambles, " times")

    win = ((win / totalGambles) * 100)  
    print(" Win Percent= ", win,"%")

    loss = ((loss / totalGambles) * 100) 
    print(" Loss Percent=  ", loss,"%")
else:
    print("please enter stake more than 0")