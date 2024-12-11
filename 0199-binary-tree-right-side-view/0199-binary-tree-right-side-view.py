# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:




        """
        Using BFS Level order traversal: Correct solution

        Main Logic
        -----------

        if i == level_length - 1:
                    result.append(node.val)

        In the inner for loop. when iteration i is at len(level_lenght) 
        Eg: len 2
            i=0
            i=1 (loop is at end: This signifies the rightmost alement which was     inserted in the queue)

            Checking if last iteration == len(level length)m - 1
            if i=1==len(2). In python it is n-1. So 1==1 (2-1=1)

        """

        if not root:
            return []
    
        result = []
        queue = deque([root])  

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                
                #checking last iteation of i is equal to length of current level -1 (in python for n-1). Last index of element signifies node facing right
                if i == level_length - 1:
                    result.append(node.val)
                
                # Add child nodes to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

        """
        Time Complexity Analysis:
Number of Nodes (n): The algorithm processes each node exactly once, visiting each node when dequeued and enqueuing its children if they exist.

Level Traversal: At each level, the algorithm performs operations proportional to the number of nodes at that level. Summing across all levels gives a total of O(n).

Queue Operations: Each enqueue and dequeue operation is O(1), contributing to O(n) overall since there are n nodes.
Overall Time Complexity:O(n)

        """

        