""" Given a non-negative integer num, repeatedly add all its digits unit
the result has only one digit"""


def addDigits(num):

    total_sum = 0
    length = len(str(num))
    print (length)
    while length >= 1:
        total_sum = total_sum + num % 10
        num = num/10
        length = total_sum
    return total_sum


print(addDigits(38))
