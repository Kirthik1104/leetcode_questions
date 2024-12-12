from collections import deque

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # BFS traversal using a queue
        queue = deque([root])
        level = 0
        
        while queue:
            length = len(queue)
            prev_val = None  # To track the previous value at the current level
            
            for _ in range(length):
                node = queue.popleft()
                
                # Validate the node value based on the level
                if level % 2 == 0:  # Even level: odd integers in strictly increasing order
                    if node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val):
                        return False
                else:  # Odd level: even integers in strictly decreasing order
                    if node.val % 2 == 1 or (prev_val is not None and node.val >= prev_val):
                        return False
                
                # Update the previous value for this level
                prev_val = node.val
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Move to the next level
            level += 1
        
        return True
