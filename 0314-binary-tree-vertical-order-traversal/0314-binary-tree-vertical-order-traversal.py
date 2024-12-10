from collections import defaultdict
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """
        Tc: The time complexity of the provided connect function is O(n), where \U0001d45b is the number of nodes in the binary tree.
        
        1) Step 1: # Store the node and the its index in the queue
        2) Pop the node and the index. Use the index as the key and node as the value
        3) For Nodes at left pointer, append the left node, index-1
        4) For Nodes at right pointer, append the right node, index +1
        5) Hashmap will save all the same nodes with same index from starting from top level to bottom level

        6) After the hashmap is build, keys would be the index which will be in sequnce of 0f -ve ...0...+ve
        7) Use a for loop with startting from min of keys to max keys +1 (n-1)---> And get all the values---> This yo u will get all the values from left   to right

        """
        if root is None:
            return []
        hashmap=defaultdict(list)
        
        queue=deque([(root, 0)])      # Store the node and the its index in the queue
     
        while queue:
            length=len(queue)
            for val in range(length):
                node, index = queue.popleft()
                hashmap[index].append(node.val)
                
                if node.left:
                    queue.append((node.left, index -1))
                if node.right:
                    queue.append((node.right, index+1))
               
        
        return [hashmap[i] for i in range(min(hashmap), max(hashmap)+1)]
        
        