class Solution:
    def rob(self, nums: List[int]) -> int:


        """
        Approach 2 Using memoization: Top down approach (same as recursion) but cahcing the already visisted values so that we dont access them again
        """
        n =len(nums)

        if n==1:
            return nums[0]
        
        if n==2:
            return max(nums[0], nums[1])
        
        memo={0: nums[0], 1: max(nums[0], nums[1])}  # Now the base case which was accessed in approach 1 using recursion will be accessed using the caching here

        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i] + helper(i-2), helper(i-1))
                return memo[i]
        return helper(n-1)

        """
        Approach 1 Using recursion---> TLE ERROR, TC: O(2^N) BECAUSE WE COMPUTING SAME VALUES AGAIN WITHOUT STORING THEM FOR EASY ACCESS
        """

        # n=len(nums)

        # if n==2:
        #     return max(nums[0], nums[1])
        # def helper(i):
        #     if i==0:
        #         return nums[0]
        #     if i==1:
        #         return max(nums[0], nums[1])            
        #     return max(nums[i]+helper(i-2), helper(i-1))
        # return helper(n-1)
        