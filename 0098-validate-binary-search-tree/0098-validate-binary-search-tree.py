# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        """
    Overall Time Complexity: The overall time complexity of the isValidBST function is 
    \U0001d442(\U0001d45b), where \U0001d45b is the number of nodes in the binary tree.
    1) a node will be always greater than -ive infinity and less than +ve infinity +ve:--> -ve <node< +ve

    2) If we travsere node.left -ive(left) will remain same but positive +ve(right) will be replaced by current node.val

                                    (- < 2 < +)
                                        2  
                        -ve            / \                 +ve
                                      1   3
                        (-ve < 1 < 2)       (2 < 3 < +ve)

    3) If we travsere node.right -ive(left) will be replaced by current node.val and positive +ve(right) will remain same

    4) since we need 3 values to work, we will create a helper fucntion and pass 3 val
        """
        def validate(node, left, right):

            if node is None:
                return True  # After compairing if left and right child reach leaf that means, it followed BST principle along the way, now return True to check other side of the tree if it follows same BST principle
    
            if not (left < node.val < right): # if condition is false, return false
                return False
                                                                    #   (node.val < node.right < +ve )
            left=validate(node.left, left, node.val)  #(nodes left value, left infinity, node's current value)

            if left== False:
                return False   # Left is not a valid BST, return false immediately

                                                                        #   (-ve < node.left < node.val )
            right = validate(node.right, node.val, right) #(nodes right value, node's current value, right infinity)

            return left and right  #(T and T), (T and F)--> output will be parsed to caller fucntion below
             
        return validate(root, float("-inf"), float("inf"))  # calling with root, neagtive and postive infinity and will return the same













        # psuedo Code
        # ----------
        # left subtree of node cotains only node  with keys less than the nodes key

        # right subtree of node contains only node with keys than the nodes key

        # Same case for left and right subtree Must aslo be BST 


        # Actual Code
        # ---------
        
        # def subtree(node, left, right):
        #     if node is None:
        #         return True
            
        #     #not (True) → False.
        #     #not (False) → True.
        #     if not (left < node.val < right):
        #         return False # If not, return False as it's not a valid BST
            
        #     left=subtree(node.left, left, node.val)    # calling the next value at left, L=-int, keep the current value as right bound

        #     if left== False:  # if any of the condition fails at left and returns false. Check left immediately and return false. No need to call the fucntion for right
        #         return False

        #     right=subtree(node.right,node.val, right)  # calling the next value at right, r=+ int, keep the current value as left bound

        #     return left and right

        # # Start the recursion with the root node and initial boundaries 
        # return subtree(root, float("-inf"), float("inf"))

        # # root, -inf (to get as min value as possible), +inf (to get as max value as possible)
        
       
        """
        Conclusion
Overall Time Complexity: The overall time complexity of the isValidBST function is 
\U0001d442(\U0001d45b), where \U0001d45b is the number of nodes in the binary tree.
        """

        
       
        