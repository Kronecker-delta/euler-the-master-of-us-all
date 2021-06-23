import math

def primetest(test):

    for count in range(int(test**0.5),1,-1):

        if test%count == 0:
            return 0
    
    return 1

smallest_number = 1
for count in range(2,20,1):

    if primetest(count) == 1:
        exp = int(math.log(20,count))
        smallest_number *= count**exp

print(smallest_number)