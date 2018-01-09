#to use the power function
import math

def square_of_the_sums(n):
    sum = 0
    for i in range(1, n+1):
        #sum up every number from 1 to the input number
        sum += i
    #square the sum
    squared = math.pow(sum, 2)
    return squared

def sum_of_the_squares(n):
    sum = 0
    for i in range(1, n+1):
        #sum up all of the sums squared
        sum += math.pow(i, 2)
    return sum

def difference(n):

    #take the output from the square of sums and subtract the output from the sum of squares
    return (square_of_the_sums(n) - sum_of_the_squares(n))

#call the function difference with the value of 100
diff = difference(100)

print "result is: %i" % (diff)
