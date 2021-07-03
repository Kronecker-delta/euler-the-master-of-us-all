from math import *


def palindromecheck(test):
    
    hold = str(test)
    reverse = hold[::-1]

    if test == int(reverse):
        return 1
    
    return 0

def primecheck1(test):

    if test == 1:
        return 0

    root = int(test**0.5)+1

    for index in range(2, root,1):

        if test%index == 0:
            return 0
    return 1


def primecheck2(test):

    if test == 1:
        return 0
    
    if test <=6 or test%6 == 1 or test%6 == 5:  
        root = int(test**0.5)

        for index in range(2, root+1,1):

            if test%index == 0:
                return 0
    
        return 1
    else:
        return 0


def smallestprimefactor(test):
    if primecheck2(test) == 1:
        return test
    
    root = int(test**2)+1
    for index in range(2,root,1):

        if test%index == 0:
            return index
        

def largestprimepower(test,prime):

    exp = 1

    power = 1

    hold = test

    while hold//power == hold/power:

        exp+=1
        power = prime**exp
    
    return exp - 1


def divisorcount(test):

    hold = test
    prod = 1

    while hold > 1:

       prime = smallestprimefactor(hold)
       power = largestprimepower(hold,prime)
       prod *= power +1
       hold = hold//(prime**power)
    return prod






