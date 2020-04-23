import itertools

def twoSum(numbers, target):
    """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
    """
    values = []
    combs = []
    for i in range(0, len(numbers)+1):
        listing = [list(x) for x in itertools.combinations(numbers, i)]
        combs.extend(listing)

    for index1 in combs:
        summ = sum(index1)
        print(len(index1), index1)
        if len(index1) > 1 and summ == target:
            indexes = index1

    if target > 0:
        for value in indexes:
            t = numbers.index(value)+1
            values.append(t)
        return values
    else:
        output = [i for i, x in enumerate(numbers) if x == 0]
        return [x+1 for x in output]


print (twoSum([-1, 0], -1))
