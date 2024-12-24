class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time Complexity: O(m * n) — we visit each cell exactly once.
        Space Complexity: O(m * n) — the maximum depth of the recursion stack can be m * n in the worst case, where
        the grid is entirely land.
        """
        rows=len(grid)
        columns=len(grid[0])
        def dfs(x, y):
            if x<0 or x>=rows or y<0 or y>=columns or grid[x][y]==0:
                return 0

            
            grid[x][y]=0

            """
            1) Counting no. of 1's in all 4 directions
            """
            area=1
            area+=dfs(x+1, y)
            area+=dfs(x-1, y)
            area+=dfs(x, y+1)
            area+=dfs(x, y-1)
            return area # returning the area for island with connected 1's

        maxi=0
        for row in range(rows):
            for col in range(columns):
                if grid[row][col]==1:
                    maxi=max(maxi, dfs(row, col)) # counting the maximum no. of 1's of an island
        return maxi # return the max count of 1's in the island from all unique island of 1's













































        
#         rows=len(grid)
#         columns=len(grid[0])

#         def matrix(row, column, grid):
#             if (row < 0 or row >= len(grid)) or \
#             (column < 0 or column >= len(grid[0])) or \
#             (grid[row][column] == 0):
#                 return 0
            
#             if grid[row][column]==1:
#                 grid[row][column]=0

#             area =1
#             area+=matrix(row+1, column, grid)
  
#             area+=matrix(row-1, column, grid)

#             area+=matrix(row, column+1, grid)

#             area+=matrix(row, column-1, grid)

#             return area
#             # print(island)
#         maxi=0
#         for row in range(rows):
#             for column in range(columns):

#                 if grid[row][column]==1:
#                     maxi=max(maxi, matrix(row, column, grid))
            
#         return maxi

