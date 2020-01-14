from collections import deque


def sortedList(low, high):
    array = []
    q = deque(range(1, 9))
    while q:
        num = q.popleft()
        if num > high:
            break
        if low <= num:
            array.append(num)
        if num % 10 + 1 < 10:
            q.append(num * 10 + (num % 10 + 1))
    return array


print(sortedList(1000, 13000))
