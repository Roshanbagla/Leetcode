def createTargetArray(nums, index):
    """
    :type nums: List[int]
    :type index: List[int]
    :rtype: List[int]
    """
    result = []
    length = len(nums)
    for i in range(length):
        result.insert(index[i], nums[i])
    print(result)

createTargetArray([1], [0])

        
