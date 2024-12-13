from collections import deque
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        # root is at index 0
        # even index level: odd integer values in increasing order
        # Odd index level: even integer in decreasing order
        """

    1) Level 0: Root node : 1 : 
        Check if node.val is odd and prev is none for root node, no need to ehck the next or, True, update prev=Current.val (anyways loop will end) so just updating

    2)Levl 1: queue[10,4]
        10 :check if node is even .val%2==0 and since its left most element prev is None is True no need to check next , set prev=current Node (10)
        4: check if node is even .val%2==0 and since since we already check prev is None is skip and go to second OR condition node < prev: 4<10 (tRUE)
    
    3) Same goes on for consecutive levels, if any of the conditions fails above, return False immdedailey, and everything is correct tree ill be accessed fully and return True in end


    4) Tc: 
    Processing Each Node: Time Complexity: O(N), where \U0001d441 is the number of nodes in the tree.
    Queue Operations: Adding children to the queue and dequeuing each node happens once per node.Time Complexity: O(N)

    Total: O(n)
    Sc: O(n)
        """


        if root is None:
            return []

        queue=deque([root])
        level=0
        while queue:

            length=len(queue)
            prev=None
            for height in range(length):
                node = queue.popleft()
                
 
                # Check if level is even
                if level%2==0:
                    if node.val%2==1 and (prev is None or node.val>prev):
                        prev = node.val
                    else:
                        return False
                # Odd level
                if level%2==1:
                    if node.val%2==0 and (prev is None or node.val<prev):
                        prev = node.val
                    else:
                        return False

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return True


        """
        Role of prev_val is None
        -----------------------
        1) At the Root Node:
            ---At the root node (level 0), there is no previous value (prev_val is None).
            ----This ensures the root node satisfies the condition without needing to compare it to a previous value.
        2) At the Leftmost Node of Any Level:
            ----For each level, prev_val is reset to None at the start of the level.
            -----The leftmost node of a level is always the first node processed, so the prev_val check ensures it satisfies the condition without requiring a comparison.


        """


        