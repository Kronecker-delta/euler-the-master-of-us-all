num = 1
num1 = 1
num3 = 1
sum = 0

while num <= 4000000:
    num1 = num + num1
    num = num3
    num3 = num1

    if num%2 == 0:
        sum += num

    
print(sum)