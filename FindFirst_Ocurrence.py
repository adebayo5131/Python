#Return the index of the first occurrence of needle in haystack,
#or -1 if needle is not part of haystack.
def strStr( haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    return haystack.find(needle)

print(strStr("Hello","ll"))
