from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=deque([root])
        result=[]
        curr=0
        while queue:
            level=[]
            length=len(queue)
            for val in range(length): 
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right) 
            if curr==0:
                result.append(level)
                curr=1
            else:
                result.append(level[::-1])
                curr=0

        return result
            

        