def isHappy(summ):
    """Find if a number is happy or not"""
    if summ != 1:
        print(square_sum(summ))
    else:
        return "True"


def square_sum(n):
    n = list(map(int, str(n)))
    sum_list = []
    total_sum = 0
    for index in n:
        square1 = index**2
        sum_list.append(square1)
    total_sum = sum(sum_list)
    w = isHappy(total_sum)
    return w


square_sum(19)
