# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr=root

        while curr:
            while curr.left:
                prev_node=curr.left

                while prev_node.right:
                    prev_node=prev_node.right

                prev_node.right=curr.right
                curr.right=curr.left
                curr.left=None
            
            curr=curr.right

        