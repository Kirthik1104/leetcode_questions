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