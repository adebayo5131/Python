from collections import deque


def sortedList(low, high):
    array = []
    # q = deque(range(1, 9))
    queue = [1,2,3,4,5,6,7,8,9]
    while queue:
        # num = queue.popleft()
        num = queue.pop(0)
        if num > high:
            break
        if low <= num:
            array.append(num)
        if num % 10 + 1 < 10:
            queue.append(num * 10 + (num % 10 + 1))
    return array


print(sortedList(1000, 13000))
