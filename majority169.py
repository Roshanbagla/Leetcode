"""Given an array of size n, find the majority element."""
"""The majority element is the element that appears """
"""more than ⌊ n/2 ⌋ times."""

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    constraint = length//2
    unique = list(set(nums))
    for index in unique:
        total_count = nums.count(index)
        if total_count > constraint:
            return index


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
