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

        """ 
        The time complexity of the algorithm is O(n) on average, where n is the number of nodes in the tree. This is because each node is visited exactly once.


        """
        curr=root

        while curr:
            if curr.left:
                prev_node=curr.left

                while prev_node.right:
                    prev_node=prev_node.right

                prev_node.right=curr.right
                curr.right=curr.left
                curr.left=None
            
            curr=curr.right

        
        """
        Why not set left = None for nodes without a left child?
        --------------------------------------------------------
        Now, for nodes that don't have a left child:

        Their left pointer is already None by default, because the TreeNode class was initialized with left=None (if no left child is provided).
        There's no need to set left = None again because it's already None.
        We only set left = None explicitly when there's an actual left child, and we move that left subtree to the right.

        """

        