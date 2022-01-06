'''
@Author: Shruti
@Date: 2022-1-2
@Last Modified by: Shruti
@Last Modified time: 2022-1-2
@Title :Write a program that takes two double command-line arguments t
and v and prints the wind chill
'''
import sys

def WindChill():
    t = float(sys.argv[1])
    v = float(sys.argv[2])

    if t > 50 or v > 120 or v < 3:
        print("Formula not valid for this conditions pls enter t<50 and v between 3 and 120")
    else:
        w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
        print("Windchill:", w)


if __name__ == '__main__': #mainfunction
    WindChill()