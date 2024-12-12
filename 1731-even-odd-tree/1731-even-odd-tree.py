from collections import deque
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        # root is at index 0
        # even index level: odd integer values in increasing order
        # Odd index level: even integer in decreasing order

        if root is None:
            return []

        queue=deque([root])
        level=0
        while queue:

            length=len(queue)
            prev=None
            for height in range(length):
                node = queue.popleft()
                
                # Check if level is even
                if level%2==0:
                    if node.val%2==1 and (prev is None or node.val>prev):
                        prev = node.val
                    else:
                        return False
                # Odd level
                if level%2==1:
                    if node.val%2==0 and (prev is None or node.val<prev):
                        prev = node.val
                    else:
                        return False

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return True


        