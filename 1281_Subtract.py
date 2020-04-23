def subtractProductAndSum(n):
    """
        :type n: int
        :rtype: int
    """
    product = 1
    sum_of_digits = 0

    while(n >= 1):
        remainder = n % 10
        print ("The remainder is ", remainder)
        n = int(n/10)
        print ("The new number is ", n)
        product = product * remainder
        sum_of_digits = sum_of_digits + remainder
    result = product - sum_of_digits
    print (result)

subtractProductAndSum (1)