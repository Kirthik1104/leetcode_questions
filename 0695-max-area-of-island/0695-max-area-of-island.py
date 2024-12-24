class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        def dfs(x, y):
            if x<0 or x>=rows or y<0 or y>=columns or grid[x][y]==0:
                return 0

            
            grid[x][y]=0

            area=1
            area+=dfs(x+1, y)
            area+=dfs(x-1, y)
            area+=dfs(x, y+1)
            area+=dfs(x, y-1)
            print(area)
            return area

        maxi=0
        for row in range(rows):
            for col in range(columns):
                if grid[row][col]==1:
                    maxi=max(maxi, dfs(row, col))
        return maxi













































        
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

