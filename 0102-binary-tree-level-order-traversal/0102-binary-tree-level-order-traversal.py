from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue=deque([root])

        res=[]

        while queue:
            nodes_list=[]

            level_size=len(queue)

            for nodes in range(level_size):

                element=queue.popleft()
                

                nodes_list.append(element.val)
   
                if element.left:
                    queue.append(element.left)
                
                if element.right:
                    queue.append(element.right)
            res.append(nodes_list)
        return res


