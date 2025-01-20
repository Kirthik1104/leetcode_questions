class Solution:
    def jump(self, nums: List[int]) -> int:
        far=0
        end=0
        n=len(nums)
        jump=0
        for i in range(n-1):
            far=max(far, i+nums[i])
            
            if i==end:
                end=far
                jump+=1

        return jump


        """
        For nums = [2, 0, 0, 1, 4], it is impossible to reach the last index. This violates the problem's guarantee that a solution exists. If this input
        were valid, it would represent an edge case the algorithm is designed to handle gracefully.
        """