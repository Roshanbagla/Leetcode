"""Given an integer n, return the number of trailing zeroes in n!."""


def trailingZeroes(n):
    if (n == 0):
        return 1
    else:
        Total = n * trailingZeroes(n-1)
        #Total = str(Total)
        return Total
        #zeros = len(Total) - len(Total.rstrip('0'))
        #return zeros


print(trailingZeroes(5))
