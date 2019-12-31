class Solution(object):
    def islandPerimeter(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # running Sum
        Sum = 0
        # number of columns
        numofCol = len(grid)

        print(len(grid))

        lengthOfRow = len(grid[0])

        for col in range(numofCol):
            for row in range(lengthOfRow):

                if grid[col][row] == 0:
                    continue

                # Above
                if col <= 0 or grid[col-1][row] == 0:
                    Sum += 1

                # Below
                if col + 1 >= numofCol or grid[col+1][row] == 0:
                    Sum += 1

                # Left
                if row <= 0 or grid[col][row-1] == 0:
                    Sum += 1

                # Right
                if row + 1 >= lengthOfRow or grid[col][row+1] == 0:
                    Sum += 1

        return Sum


testInput = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]
             ]
print(Solution.islandPerimeter(testInput))
