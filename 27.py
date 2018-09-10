def removeElement(nums, val):
    """
        :type nums: List[int]
        :type val: int
        :rtype: int
    """
    while (nums.count(val) != 0):
        nums.remove(val)
    return nums


print ((removeElement([0, 1, 2, 2, 3, 0, 4 , 2], 2))
