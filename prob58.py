def lenthOfLastWord(s):
    if s == '':
        return 0
    else:
        last_string = s.split(" ")
        length = len(last_string)
        if length == 1:
            return len(last_string[length-1])
        else:
            new_list = [x for x in last_string if x]
            new_list_length = len(new_list)
            if new_list_length == 1:
                return len(new_list[0])
            elif new_list_length > 1:
                return len(new_list[new_list_length-1])
            else:
                return 0


print(lenthOfLastWord("   day "))
