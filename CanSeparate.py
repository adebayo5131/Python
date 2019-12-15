'''
Given a non-empty String s and a dictionary wordDict containing a list of non-empty
words, determine if s can be segmeneted into a space-separated sequence of one or
more dictionary words.

Time complexity O(n^2)

Space O(n)
'''


def space_separated(s,wordDict):
    n = len(s)
    can_separated = [False for _ in range(n+1)]
    can_separated[0] = True

    for forward in range(1, n+1):
        for backward in range(forward -1,-1,-1):
            if can_separated[forward] == True:
                break

            if can_separated[backward]:
                if s[backward:forward] in wordDict:
                    can_separated[forward] = True

    return can_separated[n]


s = "Facebook"

wordDict = set(['Face', 'book', 'Facebook'])
print(space_separated(s,wordDict))
