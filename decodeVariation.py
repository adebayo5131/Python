'''
A letter can be encoded to a number in the following way:

'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'

Given a string of digits S from 0-9 representing an encoded message, return the number of ways to decode it.

Examples:

input:  S = '1262'
output: 3
explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.
Constraints:

[time limit] 5000ms

[input] string S

1 ≤ S.length ≤ 12
[output] integer


'''


def decodeVariations(S):
    if S[0] == '0':
        return 0
    previous, count = 1, 1
    for i in range(1, len(S)):
        if S[i] == '0':
            count = 0
        if S[i-1] == '1' or (S[i-1] == '2' and S[i] < '7'):
            count, previous = previous, count
            count += previous
        else:
            previous = count
    return count


S = "122231131122"
print(decodeVariations(S))
