from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        """
        The concept here is to:
        1) First get the rotten oranges and push them onto the queue
        2) Then count the number of fresh oranges


        """
        rows=len(grid)
        columns=len(grid[0])
        queue=deque([])
        fresh_oranges=0
        times=0
        for row in range(rows):
            for col in range(columns):
                if grid[row][col]==2:
                    queue.append((row, col))
                elif grid[row][col]==1:
                    fresh_oranges+=1

        """
        If the count of fresh oranges is 0, like not present in the thr grid, return 0
        """
        if fresh_oranges==0:
            return 0
    

        """
        1) From the position of rotten oranges, start exploring in all directions
        2) Why did we take levels to store the size of the queue
        3) Check the diagram, at every minute number of adjacent fresh oranges if present are rotten and our goal is to count the time required to
        rott all adjacent fresh oranges at each level---> So the level is used to rot the fresh oranges at everey minutes and even if we pop the 
        position from the queue it wont effect the current levels we are traversing---> 

        4) For every minute or levels we are in we decrement the count of fresh oranges

        5) What is minute=-1----> for minute 0 we will first find the rotten roange which is 2, and that actuall would be minute 0
            if we would have start from minute = 0,then the rotten orange which is a 2 would be minute 1, so thats the reason we started from minute=-1

        6) If by the end if the count of fresh oranges is 0 that means we have rotten all oranges which are connected to 4 directionally, if any of the fresh oraanges
        were not connected to 4 direction axis the count would not be 0

        so if count is 0 return times else -1
        """
        minute=-1
        directions=[(1,0), (-1,0), (0,1), (0,-1)]
        while queue:

            levels=len(queue)

            for level in range(levels):  #-> The levels signify each minute, level iterator is just used to traverse all adjacent node at that level
                xaxis, yaxis = queue.popleft()
                for direction in directions:
                    newx = xaxis + direction[0]
                    newy = yaxis + direction[1]

                    if (0<=newx<rows and 0<=newy<columns and grid[newx][newy]==1):
                        grid[newx][newy]=2

                        fresh_oranges-=1
                        queue.append((newx, newy))

            minute+=1
        

        return minute if fresh_oranges==0 else -1

        """
    Key Insights
    Queue: Allows simultaneous rotting of all oranges at the same level.
    
    Time Complexity: O(m×n), where m and n are the grid dimensions. Each cell is processed at most once.
    Space Complexity: O(m×n) for the queue in the worst case (all cells are rotten).
        """

        






























        # rows= len(grid)
        # columns=len(grid[0])
        # times=0
        # fresh_oranges=0
        # queue=deque()
        # for row in range(rows):
        #     for column in range(columns):
        #         if grid[row][column]==2:
        #             queue.append((row, column))
        #         elif grid[row][column]==1:
        #             fresh_oranges+=1
        
        # if fresh_oranges==0:
        #     return 0
                    
            
        # directions=[(0,1), (1,0), (0,-1), (-1,0)]
        # while queue:
        #     length=len(queue)
        #     current_time=False
            
        #     for length in range(length):
        #         row, col = queue.popleft()
        #         for direction in directions:
        #             new_row= row + direction[0]
        #             new_col= col + direction[1]
                    
        #             if (0<=new_row<rows and 0<=new_col<columns and grid[new_row][new_col]==1):
        #                 grid[new_row][new_col]=2
        #                 queue.append((new_row, new_col))
        #                 current_time=True
        #                 fresh_oranges-=1
            
        #     if current_time:
        #         times+=1

            
        # return times if fresh_oranges==0 else -1