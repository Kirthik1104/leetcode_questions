from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        queue=deque([node])
        clones={node.val:Node(node.val)}

        while queue:
            existing_node = queue.popleft()
            cloned_node = clones[existing_node.val]  # Got the value or cloned node, which will be used to append neighbours in end

            for nei in existing_node.neighbors: # Using  existing node, accessing its neighbors and mapping new node with existing node
                if nei.val not in clones:
                    clones[nei.val]=Node(nei.val)
                    queue.append(nei)
                
                cloned_node.neighbors.append(clones[nei.val])
        
        return clones[node.val]






























        # if not node:
        #     return None
        
        # cloned_node={}
        # start=node
        # stack=[start]
        # visited=set()

        # while stack:
        #     node=stack.pop()
        #     cloned_node[node]=Node(node.val)

        #     for nei in node.neighbors:
        #         if nei not in visited:
        #             visited.add(nei)
        #             stack.append(nei)
        
        # for old_node, new_node in cloned_node.items():
        #     for nei in old_node.neighbors:
        #         new_nei=cloned_node[nei]
        #         new_node.neighbors.append(new_nei)
                

        # return cloned_node[start]

        