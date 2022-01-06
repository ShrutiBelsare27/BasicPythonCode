'''
@Author: Shruti
@Date: 2022-1-4
@Last Modified by: Shruti
@Last Modified time: 2022-1-5
@Title : To Print the elapsed time.
'''
import time


class stopWatch:
    def stopWatch1(self):
        start=input("Press enter s to start time: ")
        if(start=="s"):
             start = time.time() 
             
        end=input("Press enter e to end time: ")
        if(end=="e"):
            end = time.time()
            
        elapsed_time = end - start
        print("The time elapsed is : ", elapsed_time)


T = stopWatch()
T.stopWatch1()
