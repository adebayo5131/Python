
def findMidPointCourse(pairs):

    memo = {}
    checker = {}
    mid = len(pairs)//2
    pl = len(pairs)
    start = ""

    for i in range(pl):
        memo[pairs[i][1]] = pairs[i][0]
        checker[pairs[i][0]] = pairs[i][1]
        if pairs[i][0] not in memo:
            start = pairs[i][0]

    for i in range(mid):
        start = checker[start]
    return start


pairs = [['DataStructures', 'Algorithm'],
         ['FoundationofCS', ' OperatingSystem'],
         ['ComputerNetworking', 'ComputerArchitecture'],
         ['Algorithms', 'FoundationofCS'],
         ['ComputerArchitecture', 'DatStructures'],
         ['SoftwareDesign', 'ComputerNetworking']
         ]

print(findMidPointCourse(pairs))
