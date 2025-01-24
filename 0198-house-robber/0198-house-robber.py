class Solution:
    def rob(self, nums: List[int]) -> int:

        """
        Approach 3 Using DP Array: Bottom up approach, here we will use array instead of dictionary
        Top Down Dp (Tabulation)
        Tc: O(n)
        Sc: O(n)

        Note: Notice here that we arre starting from index 2, leaving index 0 and index 1
        """
        n=len(nums)
        if n==1:
            return nums[0]
        
        if n==2:
            return max(nums[0], nums[1])

        dp=[0]*n       #---> This time we will create an array instead of dictionary to store the result

        # This will be the base cases whcih will be used when trying to access the first index or second index---> similar to one which we had in recursion
        dp[0] = nums[0]                
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):   # starting from index 2, because index 1 and index 0 is occupied by the base cases
            dp[i] = max(nums[i] + dp[i-2], dp[i-1]) # the dp array will be filled with appropirate max values at their respective index
        
        return max(dp)    # returning max of dp array


        """
        Approach 2 Using memoization: Top down approach (same as recursion) but cahcing the already visisted values so that we dont access them again : 

        Top Down Dp (Memoized)
        Tc: O(n)
        Sc: O(n)
        # """
        # n =len(nums)

        # if n==1:
        #     return nums[0]
        
        # if n==2:
        #     return max(nums[0], nums[1])
        
        # memo={0: nums[0], 1: max(nums[0], nums[1])}  # Now the base case which was accessed in approach 1 using recursion will be accessed using the caching here

        # def helper(i):
        #     if i in memo:
        #         return memo[i]       #---> Here we check if the number whihc we are trying to access already exits, if yes then return its value
        #     else:
        #         memo[i] = max(nums[i] + helper(i-2), helper(i-1)) #----> create the value in dict
        #         return memo[i]  # return the value of smaller sub probelems back to its original caller
        # return helper(n-1)

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
        