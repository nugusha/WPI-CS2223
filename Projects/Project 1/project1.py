# Nugzar Chkhaidze nchkhaidze
# project1.py



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
    print("Divide and Conquer Algorithm")
    t0 = time.clock()    # saves the starting time
    min,max=divide(alist)  # calls solution with divide and conquer method 

    print (min,max,"- min and max values")
    print (time.clock() - t0, "seconds process time")
    

def brute_force(alist):
    a=0
    b=0
    for i in alist:
        for j in alist:
            flag = 0
            for q in alist:
                if q<i:
                    flag = 1
                if q>j:
                    flag = 1
            if flag==0:
                a,b=i,j;
    return a,b

def effBF(alist):
    print("Brute Force Algorithm")
    t0 = time.clock()    # saves the starting time

    min,max=brute_force(alist)
        

    print (min,max,"- min and max values")
    print (time.clock() - t0, "seconds process time")



alist = [54,26,93,17,77,31,44,55,20]
effDC(alist)
