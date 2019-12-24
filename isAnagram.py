def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dic = {}
    re = True

    if len(s) != len(t):
        re = False
    else:
        if s == t:
            re = True
        else:
            for i in s:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1

            for j in t:
                if j not in dic:
                    re = False
                    break
                else:
                    dic[j] -= 1

            for k in dic:
                if dic[k] != 0:
                    re = False
                    break
                else:
                    re = True

    return re


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
