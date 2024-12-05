from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        hashmap=defaultdict(list)

        for index in range(len(graph)):
            if index not in hashmap:
                hashmap[index]=graph[index]
            else:
                hashmap[index].append(graph[index])
        

        def dfs(node, path):
            if node==len(graph)-1:
                result.append(list(path))
             


            for nei in hashmap[node]:
                path.append(nei)
                dfs(nei, path)
                path.pop()

            


        result=[]
        dfs(0, [0])
        return result
        
        