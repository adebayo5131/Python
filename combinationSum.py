
def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    newSet = []
    val = []
    start = 0
    candidates.sort()
    recurse(candidates, target, start, val, newSet)
    return val


def recurse(candidates, target, start, val, newSet):

    if target == 0:
        val.append(newSet)
        return

    for i in range(start,len(candidates)):
        if candidates[i] > target:
            break
        recurse(candidates, target -
                candidates[i], i, val, newSet + [candidates[i]])



print(print(combinationSum([2, 3, 5], 8)))
