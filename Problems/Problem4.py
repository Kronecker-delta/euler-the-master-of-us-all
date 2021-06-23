def palindromecheck(test):
    
    hold = str(test)
    reverse = hold[::-1]

    if test == int(reverse):
        return 1
    
    return 0

breaker = 0
for count in range(999*999,100*100,-1):

    if palindromecheck(count) == 1:

        for divisor in range(100,1000,1):

            if count % divisor == 0 and len(str(int(count/divisor))) == 3:
                print(count,divisor,count/divisor)
                breaker = 1
                break

        if breaker == 1:
            break   

    if breaker == 1:
            break  
        