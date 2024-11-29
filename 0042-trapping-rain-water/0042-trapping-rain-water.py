class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=[0]*n
        right=[0]*n
        res1=0
        res2=0

        for i in range(n):
            res1=max(res1, height[i])
            left[i]=res1

            j=n-i-1

            res2=max(res2, height[j])
            right[j]=res2

        result=0
        for i in range(n):
            result+=min(left[i], right[i])-height[i]
        return result