# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            if p.val != q.val:
                return False
            
            
            
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

            return left and right 

        return dfs(p,q)






















        # if p is None and q is None:
        #     return True 
        # if (p and not q) or (q and not p):
        #     return False 
        # if p.val!=q.val:
        #     return False 
        # left= self.isSameTree(p.left, q.left) 
        # right= self.isSameTree(p.right, q.right) 

        # return left and right 
        if p is None and q is None:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val!=q.val:
            return False

        """
        When a False value is returned from a recursive call, it goes back to the calling function, effectively ending that branch of recursion.
        """
            
        left_tree=self.isSameTree(p.left,q.left)
        if left_tree== False:                        # Here we check if any of left conditon returns false:--return false ad exit
            return False  # Early exit if left comparison fails. So the next recusion does not takes place because have already returned
        
        
        right_tree=self.isSameTree(p.right,q.right) # if the left call fails, then right wont execute 

        return left_tree and right_tree

# """
# Termination: If any of the conditions return False, the function immediately stops further checks and returns False. If all checks pass, it eventually returns True when all nodes have been verified.


# Overall Time Complexity
# Given that the function potentially visits each node once and performs a constant amount of work at each node, the overall time complexity of the function can be expressed as:
# Time Complexity=\U0001d442(\U0001d45b)

# """
        



        
