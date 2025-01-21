
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return
        
        # swapping condition
        temp=root.left
        root.left=root.right
        root.right=temp

        #recursively call left subtree and when reached none node, backtrack and call right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root























#         if root is None:   # Step 1: Base case when we reach Null nodes
#             return
        

#         # Step 2: Swap phase: 
#         temp=root.left                  # store left tree in a temp variable
#         root.left=root.right            # swap left treee with right tree
#         root.right=temp                 # swap right tree with left tree

#         # Recursively call left and right subtree
#         left=self.invertTree(root.left)
#         right=self.invertTree(root.right)

#         # Return root
#         return root

# """
# Time Complexity of the Solution
# -------------------------------
# The time complexity of this solution is O(n), where n is the number of nodes in the binary tree. Here's why:

# The algorithm performs a depth-first traversal of the tree, visiting each node exactly once.
# At each node, the algorithm:
# Swaps the left and right children.
# Recursively calls the function on the left and right children.



# Space Complexity
# --------------------
# The space complexity is determined by the call stack used during recursion:

# In the worst case (for a skewed tree), the depth of the recursion could be n (where n is the number of nodes), resulting in a space complexity of O(n).
# In the best case (for a balanced binary tree), the depth of the recursion is proportional to the height of the tree, which is O(log n).

# """
        