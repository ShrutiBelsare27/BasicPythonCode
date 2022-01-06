'''
@Author: Shruti
@Date: 2021-12-4
@Last Modified by: shruti
@Last Modified time: 2022-1-4
@Title :To print 2D array
'''
class Array:
    def Array1(self):
        matrix=[]
        row=int(input("Enter the number of rows:"))
        col=int(input("Enter the number of columns:"))

        for i in range(row):  
            a = []
            for j in range(col):
                val=int(input("Enter number: ")) 
                a.append(val)
            matrix.append(a)

        for i in range(row):
            for j in range(col):
                print(matrix[i][j], end=" ")
            print()
        
T=Array()        
T.Array1()        