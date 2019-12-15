def word_split(s,wordDict):
    n = len(s)
    solutions = {}
    solutions[n] = ['']

    def solve(i):
        if i not in solutions:
            solutions[i] = [s[i:j]+ (tail and(' ' + tail))
                            for j in range(i,n+1)
                            if s[i:j] in wordDict

                            for tail in solve(j)]
        return solutions[i]
    solve(0)
    return solutions[0]

wordDict = set(["face", "book", "facebook", "bo", "ok"])
print(word_split("facebook", wordDict))
