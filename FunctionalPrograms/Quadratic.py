'''
@Author: Shruti
@Date: 2022-1-2
@Last Modified by: Shruti
@Last Modified time: 2022-1-2
@Title :To calculate Quadratic
'''
from cmath import sqrt

class Quadratic:
    def Quadratic1(self):
        a = float(input("Enter a value: "))
        b = float(input("Enter b value: "))
        c = float(input("Enter c value: "))

        delta = b * b - 4 * a * c
        if delta>0:
            root1 = (-b + sqrt(delta)) / (2 * a)
            root2 = (-b - sqrt(delta)) / (2 * a)
            print("Two distict real roots"" root1:", root1, "\n", "root2:", root2)
        elif delta==0:
            root1=root2 = -b/(2*a)
            print("Equal is :"  , " root1:", root1, "\n", "root2:", root2)
            
        else:#delta<0
            
            #root1=root2 = -b/(2*a)
            real=-b/(2*a)
            imag= sqrt(-delta)/(2*a)
            print("Two distinct imginary roots", " root1 = ", real, " + ", imag, " i")
            print()
            print("Two distinct imginary roots"," root2 = ", real, " - ", imag, " i")


R = Quadratic()#object instantiation
R.Quadratic1()#method through object