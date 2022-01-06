'''
@Author: Shruti
@Date: 2022-1-4
@Last Modified by: Shruti
@Last Modified time: 2022-1-6
@Title : To Print start  and end time
'''
import time

def start():
        start_time = time.time()
     
        print("stopwatch is started:",start_time)
def stop():
        stop_time = time.time()
        print("stopwatch is stopped",stop_time)

flag=True

while flag:
    print("Do you want to start the stop watch?(y/n)")
    response=input("Enter y for yes ,n for no ")
    if(response=='y'):
        start()
        
    
    else:   
        stop()
        flag=False
    

        
        

        