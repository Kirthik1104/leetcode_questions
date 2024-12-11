# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        """
        1) Same logic as maximum depth
        2) Only differnce---> At each node we calcualte left height + right height and immdeaidlte set the max of it to maxi.
        3) As we are moving up backtracking from leave, at every node as we go up, maxi will be set to left + right compared with previous maxi

        4) Imagine your head as root and left hand has 5 finfer and right hand has 5 finger---> You are just doing addition of left and right and setting it to maxi

        Tc: O(n)

        """
        
        self.maxi=0
        def depth(node):
            if node is None:
                return 0

        
            left=depth(node.left)

            right=depth(node.right)
            print(left, right)


            self.maxi=max(self.maxi, left+right)

            return 1+ max(left,right)
        depth(root)
        return self.maxi