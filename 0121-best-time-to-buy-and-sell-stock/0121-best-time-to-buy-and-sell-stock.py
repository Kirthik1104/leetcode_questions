class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left=0
        right=1
        maxi=0

        while right<len(prices):
            if prices[left]<prices[right]:
                profit=prices[right]-prices[left]
                maxi=max(maxi, profit)
                # right+=1
            else:
                left=right
            right+=1
        return maxi




















        """
Time Complexity:

O(n^2): The nested loops result in a quadratic time complexity, which is inefficient for large inputs.

    Brute

        """
        # maxi=0
        # n=len(prices) 
        # for buy in range(n):              #satart at index 0
        #     for sell in range(buy+1, n):  # start from index+1: because sell should happen on next day
        #         profit=prices[sell]-prices[buy] # calcualte profit sell - buy
        #         maxi=max(maxi, profit)       # Update the max profit for every buy and sel

        # return maxi


"""
Two  pointer

Time complexity: O(n)
"""
      
        # left=0
        # right=1
        # maxi=0

        # while right<len(prices):

        #     if prices[left]<prices[right]:   #Check if price at left is less than right      

        #         profit=prices[right]-prices[left] # calcualte profit sell - buy
        #         maxi=max(maxi, profit)          # Update the max profit for every buy and sel
 
        #     else:                         #if left is greater than right
        #         left=right                # assign to right(because right is anyways smaller) and shfit right by 1
        #     right+=1                      # keep shifting right by 1 irrespective of anything
        # return maxi



        


        

















        