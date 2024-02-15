# Efficient program to print all prime factors of a given number
# https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/

import math

'''
We first take the number and divide by 2 until the number is no longer divisible by 2.
Then we divide by 3 then by 5 and so on until the number is reduced down to 1.
What was taught in school.
'''
def bruteForce(number):
    if number <= 1:
        return number
    factor = 2
    primeFactors = []
    while(number > 1):
        if (number % factor == 0):
            number = number / factor
            primeFactors.append(factor)
        else:
            if (factor == 2):
                factor += 1
            else:
                factor += 2
    print primeFactors

def squareRootApproach(number):
    if number <= 1:
        return number
    primeFactors = []
    factor = 2
    # Divide the number by 2 until it becomes odd number
    while(number%2 == 0):
        number = number / factor
        primeFactors.append(factor)
    # now starting from 3 as the factor until the square root of the number see if the number can be converted into 1
    factor = 3
    while(factor < int(math.sqrt(number))+1):
        if (number % factor == 0):
            number = number / factor
            primeFactors.append(factor)
        else:
            factor += 2
    print primeFactors, number


# Main
bruteForce(60)
squareRootApproach(60)
bruteForce(315)
squareRootApproach(315)