class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        Tc: O(n)
        """
        l=0
        r=1
        maxi=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxi=max(maxi, profit)
            else:
                l=r
            r+=1 
        return maxi

























        # left=0
        # right=1
        # maxi=0

        # while right<len(prices):  # if right reaches end that means all prices are traversed
        #     if prices[left]<prices[right]: # if prices at left is less than right
        #         profit=prices[right]-prices[left] #calculate profit
        #         maxi=max(maxi, profit) #Update the maxi
                
        #     else:         # else condition when left is > right (buy cannot be greater)
        #         left=right #setting left index to right index and always incrementing right to 1 

        #     right+=1  #even if right is greater of left is greater keep shifting the right till end
        # return maxi




















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



        


        

















        