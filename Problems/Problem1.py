num = 0

for count in range(1,1000):

    if count % 3 == 0:
        num += count
    
    if count % 3 != 0 and count % 5 == 0:

        num += count

print(num)

