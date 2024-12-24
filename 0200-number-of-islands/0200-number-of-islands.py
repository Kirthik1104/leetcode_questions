from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows=len(grid)
        columns=len(grid[0])

        # def dfs(x, y):
        #     if (x<0 or x>=rows or y<0 or y>=columns or grid[x][y]=="0"): # Base condition: Out of bound error, and grid[x][y] is 0
        #         return # Return for current position and acess the next directions
            
        #     grid[x][y]="0" # island is found(1), so change it to water, so that same position is not accessed again

        #     # Access all four directions
        #     dfs(x, y+1)
        #     dfs(x, y-1)
        #     dfs(x-1,y)
        #     dfs(x+1,y)

        # count=0
        # for row in range(rows):
        #     for col in range(columns):
        #         if grid[row][col]=="1":
        #             print(row, col)
        #             count+=1
        #             dfs(row, col)
        # return count

        def dfs(x, y):
            grid[x][y]="0"
            queue=deque([(x, y)])
            directions=[(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                xaxis, yaxis = queue.popleft()
                for direction in directions:
                    new_x = xaxis + direction[0]
                    new_y = yaxis + direction[1]

                    if (0<=new_x<rows and 0<=new_y<columns):
                        
                        if grid[new_x][new_y]=="1":
                       
                            grid[new_x][new_y]="0"
                            queue.append((new_x, new_y))
                        
        count=0
        for row in range(rows):
            for col in range(columns):
                if grid[row][col]=="1":
                    count+=1
                    dfs(row, col)
                    print(row, col)

        return count






























        
#         def matrix(row, column):
#     # Check if the current position is out of bounds or if it's already visited (0)
#             if (row < 0 or row >= len(grid)) or \
#             (column < 0 or column >= len(grid[0])) or \
#             (grid[row][column] == "0"):
#                 return
            

            
#             # If the cell is part of an island (1), mark it as visited (0)
#             if grid[row][column] == "1":
#                 grid[row][column] = "0"

            
        

#             # Explore all four directions (down, up, right, left)
#             matrix(row + 1, column)  # down

#             matrix(row - 1, column)  # up

#             matrix(row, column + 1)  # right

#             matrix(row, column - 1)  # left


    


#         rows = len(grid)
#         columns = len(grid[0])

#         island = 0
#         for row in range(rows):
#             for col in range(columns):
#                 if grid[row][col] == "1":  # Only start grid search if we find an unvisited land
#                     island+=1
#                     matrix(row, col)
                    
#         return island





























#         if not grid:
#             return
        
#         length_rows=len(grid)
#         length_columns=len(grid[0])

#         island=0

#         """
#         Input: grid = [
#         ["0#","1","1","1","0"],
#         ["1","1","0","1","0"],
#         ["1","1","0","0","0"],
#         ["0","0","0","0","0"]
#         ]
#         """
#         def bfs(row, column):
#             grid[row][column]="0"
#             queue=deque([(row, column)])

#             directions=[(0,-1), (0, 1), (-1,0), (1,0)]

#             while queue:

                
#                 for direction in directions:
#                     existing_row, existing_col = queue.popleft()

#                     new_row= existing_row + direction[0]

#                     new_col= existing_col + direction[1]

#                     if(0 <=new_row < length_rows and 
#                     0 <=new_col < length_columns and
#                     grid[new_row][new_col]=="1"):

#                         grid[new_row][new_col]="0"

#                         queue.append((new_row, new_col))










#         """
#         1) This two for loops will find the first one
#         2) When we find the first 1, we will update the island to 1 and call the
#         bfs with current row and column where we got 1 

#         3) The role of BFS: When we call the bfs with the current row and col postion, its store the position in queue and travserse all the four direction from its current position and marks 1 to zero (making it visited).

#         4) if the queue is empty, it returns and the for loops tries to access the nesxt 1

#         5) if there is a single 1 surrounded by water thats a distinct island
#         6) And all the connected 1's forms a single island

#         """    

#         for row in range(length_rows):
#             for column in range(length_columns):
#                 if grid[row][column]=="1":
#                     island+=1
#                     bfs(row, column)

#         return island



#         # """
#         # Time Complexity: O(m * n): Since we will visit each cell once.
#         # M is column
#         # N is row

#         # Space complexity is min(m,n): due to the queue used in BFS
#         # ""'

