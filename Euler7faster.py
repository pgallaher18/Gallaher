import math


#1 is not prime, so skip it
potential_prime = 2

counter = 0

#continue to loop until 10001 prime found
while (counter < 10001):
    #increment counter by 1
    counter += 1
    #range of divisor starts at 2
    #divide by every number from 2 to the square root
    #add one to make the range inclusive
    for number in range(2, int(math.floor(math.sqrt(potential_prime)))+1):
        #if no remainder
        if ((potential_prime % number) == 0):
            counter -= 1
            break
    potential_prime += 1

#subtract one
print potential_prime - 1
