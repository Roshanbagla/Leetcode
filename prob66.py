def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = map(str, digits)
        string = ''.join(string)
        string = int(string)
        string = string + 1
        list = [int(d) for d in str(string)]
        return list


print(plusOne([9, 8]))
