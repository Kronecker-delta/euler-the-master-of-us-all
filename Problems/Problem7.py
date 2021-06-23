def primetest(test):

    for count in range(int(test**0.5),1,-1):

        if test%count == 0:
            return 0
    
    return 1

count = 0
test = 2
while count < 10001:

    if primetest(test) == 1:
        count += 1
        
    test += 1
       
print(test-1)