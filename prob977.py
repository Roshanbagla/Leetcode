def sortedSquares(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        length = len(A)
        B = []
        for index in range(0, length):
            B.append(A[index]**2)
        B.sort()
        return (B)


print(sortedSquares([-4, -1, 0, 3, 10]))
