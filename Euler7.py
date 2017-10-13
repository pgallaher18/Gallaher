import math

#1 is not prime, so skip it
potential_prime = 2
#empty list to hold all primes
list_of_primes = []

#continue to loop until 10001 prime found
while (len(list_of_primes) < 10001):
    #add potential number to list
    list_of_primes.append(potential_prime)
    #check all potential divisors up until the square root is rounded up
    for number in range(2, int(math.floor(math.sqrt(potential_prime)))+1):
        #if no remainder
        if ((potential_prime % number) == 0):
            #remove it from the list
            list_of_primes.remove(potential_prime)
            #stop looping, go to next iteration
            break
    #next prime to check
    potential_prime += 1

#10001 element
print list_of_primes[10000]
