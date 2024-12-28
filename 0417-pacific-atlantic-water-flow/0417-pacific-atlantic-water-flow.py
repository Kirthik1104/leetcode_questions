from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        """
        1) How We will find a solution for this problem

        --> We will use two seperate queues to seperately store the positions which touches both  pacific ocean and atlantic ocean
        --> Important: We will use two seperate sets to store the postions of both pacific and atlantic ocean---> In the end, the intersection of this sets which will gives us common position in both sets, will be the answer

        2) How to approach this problem
        --> Use a two seperate queus to store the postions which touches pacific and talntic ocean positions seperately
        --> Use two different sets to to store all the position so that we dont visit them again

        --> After creating this, start a bfs for each combination of pqueue, pseen and qqueue and aseen.
        --> from the edge posotions which touches the ocean, start a bsf and check 
        -->  check if the new position is greater than current posotion, that means water can flow from greater height to lower height
        --> Store the visited positions in a set

        --> In the end this set will give us positions which are common in both pseen and aseen

        """
        if not heights:
            return heights

        rows=len(heights)
        columns=len(heights[0])


        pq=deque()
        pseen=set()

        aq=deque()
        aseen=set()

        for row in range(rows):
            pq.append((row, 0))
            pseen.add((row, 0))

            aq.append((row, columns-1))
            aseen.add((row, columns-1))

        for column in range(columns):
            pq.append((0, column))
            pseen.add((0, column))

            aq.append((rows-1, column))
            aseen.add((rows-1, column))
        
        def bfs(q, seen):

            while q:
                directions=[(1,0), (-1,0), (0,1), (0,-1)]
                x, y = q.popleft()
            
                for direction in directions:
                    newx = x + direction[0]
                    newy = y + direction[1]

            # Condition to check in bounds. 
            # What is not in seen? --> It is used to avoid all the border cells revisiting again and also avoid visiting same positions again
            # Also checking if new position is greater than th existing position 
                    if (0<=newx<rows and 0<=newy<columns and (newx, newy) not in seen and heights[newx][newy] >= heights[x][y]):
                        q.append((newx, newy))
                        seen.add((newx, newy))



        bfs(pq, pseen)
        bfs(aq, aseen)
        print(pseen, aseen)
        return list(pseen.intersection(aseen))




































        # if not heights:
        #     return []

        # # Creating a queue for pacific ocean and atlantic ocean
        # pq=deque()
        # aq=deque()

        # # Creating a set for pacific ocen and atlantic ocean
        # pseen=set()
        # aseen=set()

        # row = len(heights)
        # column = len(heights[0])

        # # Adding elements from top column
        # for j in range(column):
        #     pq.append((0, j))
        #     pseen.add((0,j))

        # # Adding elements from the left row
        # for i in range(row):
        #     pq.append((i, 0))
        #     pseen.add((i, 0))

        # # Adding elements from the bottom column
        # for j in range(column):
        #     aq.append((row-1, j))
        #     aseen.add((row-1, j))
        
        # # Adding elements from the right row
        # for i in range(row):
        #     aq.append((i, column-1))
        #     aseen.add((i, column-1))
        

        # def bfs(q, seen):

        #     while q:
        #         i, j = q.popleft()

        #         for ioff, joff in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        #             r = i + ioff
        #             c = j + joff

        #             if (0<=r<row and 0<=c<column and (r,c) not in seen and heights[r][c]>=heights[i][j]):
        #                 q.append((r,c))
        #                 seen.add((r,c))

        
        # bfs(pq, pseen)
        # bfs(aq, aseen)
        # print(pseen)
        # print(aseen)

        # result= list(pseen.intersection(aseen))
        # return result
        
        