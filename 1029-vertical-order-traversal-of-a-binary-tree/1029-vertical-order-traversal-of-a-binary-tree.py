from collections import deque
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        """

        Tc:
        ----
        Combining all parts:

        1)BFS traversal: O(N).
        2)Sorting nodes within columns: O(NlogN).
        3)Sorting columns: O(klogk), where k≤N.
        4)Extracting results: O(N).
        5)The overall complexity is dominated by the sorting operations, so:

        Total Time Complexity: O(NlogN)

        Sc:
        ----

        Space Complexity
        1) Queue:
        The BFS queue stores nodes level by level. In the worst case (complete binary tree), the queue can hold at most half the nodes at the last level: O(N).

        2) HashMap:
        The hashmap stores all N nodes grouped by columns. Space required: O(N).

        3) Intermediate Storage:
        The nodes for each column are stored temporarily for sorting: O(N).
        Total Space Complexity: O(N)
        """
        hashmap={}

        hashmap=defaultdict(list)

        queue=deque([(root, 0, 0)])

        while queue:

            length=len(queue)

            for val in range(length):
                node, row, col = queue.popleft()

                hashmap[col].append((row, node.val))  # Storing column as keys (cauuse column moves left to right and (row, val) as values)


                if node.left:
                    queue.append((node.left, row+1, col-1))
                
                if node.right:
                    queue.append((node.right, row+1, col+1))

      

            """
            1) For loop: sort the columns (keys) first (-2,-1,0,1,2)
            2) node = sorted(hashmap[col])     # sort the values inside each column (row, val). if multiple values present (row, val), (row, val) sorted will first sort by row and if rows are same, it will sort by values.------> Why we sort by rows?----> rows means top to bottom level, in a standing column if you want values from top to bottom you will first sort by rows to get the val at the top row.-----> what is same rows are present, that means 2 values present at same row level, then sorted will sort by values. 

            """
            result=[]
            for col in range(min(hashmap), max(hashmap)+1):     # sort the columns (keys) first (-2,-1,0,1,2)
                node = sorted(hashmap[col])     # sor the values inside each column (row, val). if multiple values present (row, val), (row, val) sorted will first sort
                extract=[val for row, val in node]
                result.append(extract)
        return result


 





        
        