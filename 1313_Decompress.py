def decompressRLElist(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        length = len(nums)
        if length == 1:
            result.append(nums)
        if length == 2:
            for i in range(0,length-1):
                [freq, value] = nums[2*i], nums[2*i+1]
                for j in range(0, freq):
                    result.append(value)
        if length > 2:
            for i in range(0,length/2):
                [freq, value] = nums[2*i], nums[2*i+1]
                for j in range(0, freq):
                    print("The value of J is :", j)
                    result.append(value)
        print (result)

decompressRLElist([55,11,70,26,62,64,12,45,1,66])