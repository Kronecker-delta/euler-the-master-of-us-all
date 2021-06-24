def primetest(test):

    for count in range(int(test**0.5),1,-1):

        if test%count == 0:
            return 0
    
    return 1

sum = 0
for count in range(2,2000000,1):

    if primetest(count) == 1:
        sum += count

print(sum)