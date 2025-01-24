# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            print("hi")
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            if p.val!=q.val:
                return False
            
            left = dfs(p.left, q.left)
            right= dfs(p.right, q.right)

            return left and right

       
        if not subRoot:                         # if only given subroot does not exis, return true cause root can be subroot of itself
            return True
        if not root:                            # if we reach none node, or if root node does not exist return False
            return False
        
        if root.val==subRoot.val:       #only call the same tree fucntion, when you see matching value, other dont call same tree, reducing unnecessary fucntion call
            if dfs(root, subRoot):
                return True
              
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)  # compare T or f, f or f
      















        """
        First try
        """

        if not subRoot:
            return True
        if not root:
            return False
        
        if self.issame(root, subRoot):
            return True

     
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def issame(self, root:Optional[TreeNode]=None, subRoot:Optional[TreeNode]=None)->bool:

        if root is None and subRoot is None:
            return True
        if (root and not subRoot) or (subRoot and not root):
            return False
        if root.val!=subRoot.val:
            return False
        
        left=self.issame(root.left, subRoot.left)
        right=self.issame(root.right, subRoot.right)

        return left and right


       

    
