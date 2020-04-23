def solution(message, K):
    # write your code in Python 3.6
    current_message = message.split(' ')
    print (current_message)
    # step 1: if message length is less than K then returns original message
    length = len(message)
    if length < K:
        return message

    # step 2: refining a message
    new_message = message[:K]
    new_message = new_message.split(' ')
    for index in range(0, len(new_message)):
        if not(current_message[index] == new_message[index]):
            del new_message[index:]

    # check if last element is a space or not
    space_length = len(new_message)
    if (new_message[space_length-1] == ''):
        new_message.pop(space_length-1)
        return (' '.join(new_message))
    return (' '.join(new_message))


print(solution("The quick brown fox jumps over the lazy dog", 39))
