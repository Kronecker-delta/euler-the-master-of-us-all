for first_number in range (1,1000,1):

    for second_number in range(first_number+1,1000,1):

        if 2*second_number*(first_number+second_number) == 1000:

            first_factor = 2*first_number*second_number
            second_factor = second_number**4-first_number**4
            print(first_factor*second_factor)
            exit()