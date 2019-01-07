#Runtime ~140s.

#Returns False if n divides m with no remainder, otherwise returns True.
def uneven_divisor(m, n):
    if m % n == 0: return False
    return True

#Finds smallest integer that is evenly divisible (i.e. with no remainder) by numbers from 1 up to max_divisor.
def smallest_multiple(max_divisor):
    count = max_divisor #A lower bound for the smallest integer is max_divisor.
    min_divisor=int(max_divisor/2) #The smallest divisor required to be checked is floor(max_divisor/2) since if a number is divisible from all numbers between and including min_divisor and max_divisor, then it follows that it is also divisible by those numbers between 1 and min_divisor.
    unfinished = True
    while unfinished:
        #Check if the candidate number has any remainders from any of the divisors.
        for n in range(min_divisor, max_divisor + 1)[::-1]: #Count backwards because the larger the number, the more likely it is to divide with a finite remainder, leading to a faster break.
            if uneven_divisor(count, n):
                count += 1
                break
            #If no divisors, then the smallest integer has been found.
            if n == min_divisor and uneven_divisor(count, min_divisor) == False:
                unfinished = False
                return count

print(smallest_multiple(20))
