from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        """
        Maximum Depth: Root node to deepest node------> No. of node nodes from root to deepeest node.
        ------------------------------------------------------------------------------------------
                   1
                /     \
               2       3
              / \
             4   5
            /
           8
    
        At 8: left None and Right None
        left_tree got 0 and right tree got 0
        max(left, right)--> get max depth of either left or right: Both are 0 so---> +1 (0,0)-->+1 for current node which is 8--> return 1 to 4

        At 4: Left returned 1 from 8 and right is None so 0
        left=1 and right =0
        1+max(left,right)--> left is 1 and right is 0 (no nodes), max of left and right is left=1, which has one extra node on left (8) and none on right
        1+(1,0)= add 1 for current node(4) and pass it to previous call-->1+1=2

        At Node 2:
        left=2 (node 4 and 8), right=1 (only 1 node 5)
        from 2 left has 2 nodes and right has 1 node. that means left depth is greater than right depth of 1
        1+max(left,right)--->1+(2,1)---->1+2==3---> return 3 to previous call
        
        At noDE 1
        left=3 right=1

        left depth is greater than right depth
        1+max(left, right)---->1+(3,1)---->1+3---->4  (+1 fpr current node 1)



        1)
        """
        if root is None:
            return 0
        left_tree=self.maxDepth(root.left)
        right_tree=self.maxDepth(root.right)
        return max(left_tree,right_tree)+1

        """
        why return +1 with max(left_tree, right tree)--> +1 is used to include the current node in the depth calculation and pass that value back to the previous recursive call.
        """




















        #Using BFS

        # Iterative approach using BFS: Using deque and for loop
        # if root is None:
        #     return 0
        
        # depth=0
        # queue=deque([root])

        # while queue:

        #     node_length=len(queue)

        #     for i in range(node_length):
        #         node=queue.popleft()

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)

        #     depth+=1
        # return depth


        """
        In summary:

Time Complexity: O(n) (where n is the number of nodes in the tree).
Space Complexity: O(d) (where d is the maximum number of nodes at any level, which in the worst case is O(n)).
        
        """


        #Uinsing recursion


        if root is None:
            return 0

        left=self.maxDepth(root.left)

        right=self.maxDepth(root.right)


        return 1+max(left, right)
        
"""        
Time Complexity
--------------
Why O(n)?
Both approaches must visit each node exactly once to determine the depth. This involves either a Depth-First Search (DFS) in the recursive approach or a Breadth-First Search (BFS) in the iterative approach.
"""