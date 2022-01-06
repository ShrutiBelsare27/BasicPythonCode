'''
@Author: Shruti
@Date: 2021-12-30
@Last Modified by: Shruti
@Last Modified time: 2021-12-30 
@Title : String replace
'''

 
userName=input("Please enter your name :") 
if userName.isalpha(): 
    if len(userName)>3: 
        print("Hello",userName," How are you ?")
    else:
        print("Please enter more than 3 characters")
else: 
    print("Not a valid input string")