"""Find the longest Prefix string among strings."""
import os


def longestCommonPrefix(strs):
    """function body."""
    if strs:
        return os.path.commonprefix(strs)
    else:
        return ""


print(longestCommonPrefix(['flower', 'flow', 'flight']))
