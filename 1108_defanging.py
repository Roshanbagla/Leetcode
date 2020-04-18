def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    return address.replace(".","[.]",4)


defangIPaddr("255.100.50.0")