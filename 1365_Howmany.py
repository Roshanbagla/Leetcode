def smallerNumbersThanCurrent(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        result = []
        length = len(nums)
        if length == 1:
            return nums
        if length >= 2:
            for i in range(0, length):
                for j in range(0, length):
                    if ((j!=i) and (nums[j]< nums[i])):
                        count = count + 1
                result.append(count)
                count = 0
        print (result)


smallerNumbersThanCurrent([8,1,2,2,3])       

