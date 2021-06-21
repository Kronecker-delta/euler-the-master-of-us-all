def primecheck(test):
    num1 = int(test**0.5)

    for div in range(num1,1,-1):
        if  test % div == 0:
            return 0
    
    return 1


num = 600851475143
root = int(num**0.5)

for fac in range(root,0,-1):
    if num % fac == 0 and primecheck(fac) == 1:
        break

print(fac)
