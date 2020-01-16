
def canReach(arr, start):
    """
    :type arr: List[int]
    :type start: int
    :rtype: bool
    """

    if start >= len(arr) or start < 0:
        return False

    if arr[start] == float("-inf"):
        return False

    if arr[start] == 0:
        return True

    current = arr[start]

    # Changed its value to indicated seen
    arr[start] = float("-inf")

    return canReach(arr, start + current) or canReach(arr, start - current)


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5
print(canReach(arr, start))
