def solution(S, K):
    # write your code in Python 3.6
    Days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    remainder = K % 7
    position = Days.index(S)
    new_position = position + remainder
    if (new_position < 7):
        return Days[new_position]
    else:
        new_position = new_position % 7
    return Days[new_position]


print(type(solution("Wed", 2)))
