# Nugzar Chkhaidze nchkhaidze
# project1
# The code implements two methods, Brute Force and Divide & Conquer(recursive)
# methods to find minimum and maximum values in an array with randomly generated
# numbers. The code lets you choose the method and a size of array small, medium or large
# 

import time
import random

# divide(alist) gets a list as an input 
# and returns minimum and maximum values in it
def divide(alist):
    if len(alist)>1:  
        mid = len(alist)//2     #finds point to split list
        lefthalf = alist[:mid]  #splits list in two parts
        righthalf = alist[mid:]
        min1,max1=divide(lefthalf) # solves subtask for left part
        min2,max2=divide(righthalf) # solves subtask for right part

        return min(min1,min2),max(max1,max2) # combines answers for
                         # left and right subtasks and returns them  

    elif len(alist)==1:    # returns the value as max and min if
        return alist[0],alist[0] # there is only 1 number
    
def effDC(alist):
    print("Divide and Conquer Algorithm  - O(n)")
    t0 = time.clock()    # saves the starting time
    min,max=divide(alist)  # calls solution with divide and conquer method 

    print (min,max,"- min and max values")
    print (time.clock() - t0, "seconds process time")

def brute_force(alist):
    a=0  # final minimum
    b=0  # final maximum 
    for i in alist:
        for j in alist:
            flag = 0
            for q in alist:
                if q<i:   # check if any number is smaller than i
                    flag = 1
                if q>j:   # check if any number is bigger than j
                    flag = 1
            if flag==0:
                a,b=i,j;
    return a,b

def effBF(alist):
    print("Brute Force Algorithm  - O(n^3)")
    t0 = time.clock()    # saves the starting time

    min,max=brute_force(alist)
        

    print (min,max,"- min and max values")
    print (time.clock() - t0, "seconds process time")


while (1):
    print("Type 1 for array sized 10");
    print("Type 2 for array sized 50");
    print("Type 3 for array sized 200");
    print("Type 4 to Quit");
    x = int(input())

    if x==4:
        print("Thank you!")
        break
    elif x==1:
        n = 10
    elif x==2:
        n = 50
    elif x==3:
        n = 200
    else:
        print("Wrong number! Try again")
        continue

    alist = [random.randint(1,1000) for _ in range(n)]
        # creates a list with n numbers
        
    for x in alist:
        print(x,end=' ')
    print()

    print("Array size is ",n)

    effDC(alist) ## calls divide and conquer solution
    effBF(alist) ## calls brute forces solution
    print('\n')
