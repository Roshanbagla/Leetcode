"""An Integer is a palindrome."""


def isPalindrome(number):
    """To check if an integer is a palindrome."""
    reverse = number[::-1]
    if number == reverse:
        return True
    return False


number = input()
print(isPalindrome(number))
