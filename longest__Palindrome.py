def longestPalindrome(s):
    freq = {}

    for i in s:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    odd = 0
    ret = 0
    for k in freq:
        if freq[k] % 2 == 0:
            ret += freq[k]
        else:
            ret += freq[k] - 1
            odd = 1
    return ret + odd


print(longestPalindrome("abccccdd"))
