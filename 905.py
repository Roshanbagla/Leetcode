"""Sort Array by Parity."""


def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    even_list = []
    odd_list = []
    for index in A:
        if index > 1 and index % 2 == 0:
            even_list.append(index)
        elif index == 0:
            even_list.append(index)
        else:
            odd_list.append(index)

    return even_list+odd_list


print(sortArrayByParity([3, 1, 2, 4]))
