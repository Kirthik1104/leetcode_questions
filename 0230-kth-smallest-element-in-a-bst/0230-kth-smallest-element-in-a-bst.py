# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        1) kth smallest value means : imagine a sorted array from 1 to 10, if k 3, then elemnt 3 is the kth smallest element
        2) Over here, if you look at the BST, it follows a BST property: left is smaller and right is big
        3) And when we say that we are looking for smallest element, it is obvious to check the left subtree and then right--> Pricesaly left--root--right
        4) Why in-order traverasl is suitable, check the tree, left most element is smallest (2) and then the root (3) and then the right element (4)
        5) ouR goal is to travser till the leftmost element ( we found the smallest:--2) increment the counter and check if it equal to the kth smallest index (given index), if not then
        check root (3) which is 2nd smallest, then 4 (3rd smallest)

        6) If we counter matches the k, store in a object variable, why? ---> so that you can preserve it and return in the end

        Eg imagine k=3 : 
                    go till left 2 : counter 1 (left and right both none) ...1! = k
                    go to root 3 : counter 2 2!=k
                    go to root 4 : counter 3 3==k (3) --> store tha nodes value at counter 3 or index k self.result = node.val

                    in the return the self.result

            Tc: O(n)--> No. of nodes in the tree

                5
                /   \
                3     8
            / \   / \
            2   4 6   9


        """
        def dfs(node):
            if node is None:
                return
        

            # In order Traversal  left--->root--->right

            dfs(node.left)         # go left
            self.counter+=1        # start updating the counter
            if self.counter == k: 
                self.result = node.val  # store the node.value when it matchines the desired kth index in a variable seperately
            dfs(node.right)       # Go right

        self.counter=0
        self.result= 0
        dfs(root)
        return self.result
     