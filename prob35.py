def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        maximum = max(nums)
        if target in nums:
            return nums.index(target)
        elif target < maximum:
            for index in range(0, len(nums)):
                if not(nums[index] < target):
                    return index
        else:
            return nums.index(maximum)+1


print(searchInsert([1, 3, 5, 6], 5))
