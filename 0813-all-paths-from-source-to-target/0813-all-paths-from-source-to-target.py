class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):
            # Add the current node to the path
            path.append(node)

            # If we reach the target node, add the current path to the result
            if node == len(graph) - 1:
                result.append(list(path))
            else:
                # Recursively explore each neighbor
                for neighbor in graph[node]:
                    dfs(neighbor, path)

            # Backtrack: Remove the current node from the path
            path.pop()

        result = []
        dfs(0, [])  # Start DFS from node 0 with an empty path
        return result
