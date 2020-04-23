def rob(nums):
    """
        :type nums: List[int]
        :rtype: int
    """
    if len(nums) == 0:
        return 0
    c = [0] * len(nums)
    length = len(nums)
    c[0] = nums[0]
    c[1] = max(nums[0], nums[1])
    for index in range(2, length):
        c[index] = max(nums[index] + c[index - 2], c[index - 1])

    return max(c)


print(rob([0]))
