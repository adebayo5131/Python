'''You are giving a number and you want to know the minimum amount of steps required
until you can get frpm n to 1

Available steps
Decrement by 1
if n is divisble by 2 then divid by 2
if n is divisble by 3 then divid by 3

Example         #Result
10 => 3 steps ( 10-->9-->3-->1)
15 => 4 steps (15 --> 5 --> 4 -->2 -->1)'''

# Using memoization
# import sys
# sys.setrecursionlimit(100000)


# def getminSteps(n, memo):
#     # base case
#     if n == 1:
#         return 0

#     if memo[n] != 0:
#         return memo[n]

#     result = getminSteps(n-1, memo)

#     if (n % 2 == 0):
#         result = min(result, getminSteps(n//2, memo))
#     if (n % 3 == 0):
#         result = min(result, getminSteps(n//3, memo))

#     memo[n] = result + 1
#     return memo[n]


# n = 1000
# memo = [0 for i in range(n+1)]
# print(getminSteps(n, memo))

'''without memoization'''
# def getminSteps(n):
#     # base case

#     if n == 1:
#         return 0


#     result = getminSteps(n-1)
#     if (n % 2 == 0):

#         result = min(result, getminSteps(n/2))


#     if (n % 3 == 0):
#         result = min(result, getminSteps(n/3))

#     return result+1


# print(getminSteps(20))

'''Bottom up approach using tabulation'''


def getminSteps(n):
    table = [50 for i in range(n+1)]
    table[1] = 0

    for i in range(1, n):
        table[i+1] = min(table[i+1], table[i]+1)
        if (i*2 <= n):
            table[i*2] = min(table[i]+1, table[i*2])
        if (i*3 <= n):
            table[i*3] = min(table[i]+1, table[i*3])
    return table[n]


n = 6000
print(getminSteps(n))
