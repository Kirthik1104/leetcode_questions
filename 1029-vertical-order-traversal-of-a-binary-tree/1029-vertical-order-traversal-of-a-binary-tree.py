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
        hashmap={}

        hashmap=defaultdict(list)

        queue=deque([(root, 0, 0)])

        while queue:

            length=len(queue)

            for val in range(length):
                node, row, col = queue.popleft()

                hashmap[col].append((row, node.val))


                if node.left:
                    queue.append((node.left, row+1, col-1))
                
                if node.right:
                    queue.append((node.right, row+1, col+1))
           
            result=[]
            for col in sorted(hashmap):
                node = sorted(hashmap[col])
                extract=[val for row, val in node]
                result.append(extract)
        return result


 





        
        