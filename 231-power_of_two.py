""" Given an integer, write a function to determine if it is a power of two."""

def isPowerOfTwo(n):

    if (n > 0 and n <= 2):
        return True
    elif (n > 2):
        value = 1
        power = 2
        while (n > power):
            power = 2**value
            value += 1
        value = 2**(value - 1)
        if (value == n):
            return True
        else:
            return False
    else:
        return False


print(isPowerOfTwo(1))
