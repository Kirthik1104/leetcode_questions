class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda pair: pair[0]-pair[1])

        n=len(costs)
        result=0
        for i in range(n//2):
            result+=costs[i][0]
        for i in range(n//2, n):
            result+=costs[i][1]
        return result

