def solution(A):
    # write your code in Python 3.6
    A = str(A)
    if len(A) <= 2:
        return int(A)
    return int((A[0] + A[-1] + str(solution(A[1:-1]))))


print(solution(123456))
