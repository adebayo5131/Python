# def look_and_say(n):
#     def next_number(s):
#         result, i = [], 0
#         while i < len(s):
#             count = 1
#             while (i + 1) < len(s) and s[i] == s[i + 1]:
#                 i += 1
#                 count += 1
#             result.append(str(count) + s[i])
#             i += 1
#         return "".join(result)
#     s = '1'
#     for _ in range(1, n):
#         s = next_number(s)
#     return s


# print(look_and_say(4))
def countAndSay( n):
    """
    :type n: int
    :rtype: str
    """
    if n==1:
        return '1'
    else:
        s = self.countAndSay(n-1)
        
        count = 1
        retS=''
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                retS+=str(count)+s[i-1]
                count=1
            else:
                count+=1
        retS+=str(count)+s[len(s)-1]
        return retS
print(countAndSay(4))