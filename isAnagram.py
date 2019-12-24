def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dic = {}
    re = bool

    if len(s) != len(t):
        return False

    if s == t:
        return True

    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for j in t:
        if j not in dic:
            return False
        else:
            dic[j] -= 1

    for k in dic:
        if dic[k] != 0:
            return False
        else:
            return True


s = "anagram"
t = "nagarak"
print(isAnagram(s, t))
