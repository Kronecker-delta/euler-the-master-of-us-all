sum = 0

for count in range(1, 101, 1):
    
    for index in range(1,101,1):

        if index == count:
            index = 0
        
        sum += count*index

print(sum)