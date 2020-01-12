def isIsomorphic( w1, w2):
    """
    :type s: str
    :type t: str
    :rtype: bool
        """
    isomorphicDic = {}

#         if  len(w1) == ''and len(w2) =='':
#             return True    
#         if len(w1) != len(w2):
#             return False

    for key in range(len(w1)):
        if w1[key] in isomorphicDic:
            if isomorphicDic[w1[key]] != w2[key]:
                return False
        else:
            if w2[key] in isomorphicDic.values():
                return False
            else:
                isomorphicDic[w1[key]] = w2[key]
    return True

print(isIsomorphic("egg","add"))