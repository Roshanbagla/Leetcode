def addBinary(a, b):
    """
        :type a: str
        :type b: str
        :rtype: str
    """
    sum = bin(int(a, 2) + int(b, 2))
    print(sum[2:])


addBinary('00001', '10001')
