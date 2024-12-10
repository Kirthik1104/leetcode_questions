# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return root

        def dfs(s1, s2):

            if s1 is None and s2 is None:
                return True
            
            if (s1 and not s2) or (s2 and not s1):
                return False
            
            if s1.val!=s2.val:
                return False
            
            left=dfs(s1.left, s2.right)
            right=dfs(s1.right, s2.left)

            return left and right
        
        if  (root.left and not root.right) or (root.right and not root.left) :
            return False
        if dfs(root.left, root.right):
            return True
        return False

        
        