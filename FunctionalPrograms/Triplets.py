'''
@Author: Shruti
@Date: 2022-1-2
@Last Modified by: Shruti
@Last Modified time: 2022-1-2
@Title :To print the distinct triplets
'''
import math
def triplets(arr,arr_len, sum):

    for i in range(0, arr_len - 2):

        for j in range(i + 1, arr_len - 1):

            for k in range(j + 1, arr_len):

            
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                        

arr = [int(i) for i in input().split()]

arr_len = len(arr)
sum=0
triplets(arr,arr_len, sum)

