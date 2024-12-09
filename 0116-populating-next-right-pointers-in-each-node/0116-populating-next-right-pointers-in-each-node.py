from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue=deque([root])
        while queue:
            level=[]
            length=len(queue)
            for val in range(length):
                node=queue.popleft()
                if node:
                    level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            for i in range(len(level)):
                if len(level)==1:
                    node=level.pop(0)
                    node.next=None
                else:
                    node1=level.pop(0)
                    node2=level[0]
                    node1.next=node2
        return root
    