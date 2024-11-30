class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        hashset=set()
        res=0
        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left+=1



            hashset.add(s[right])
            res=max(res, right-left+1)
        return res




        """
        Brute Force Approach: O(n^2)
        """
        # maxi=0             # max to keep track of maximum value

        # for i in range(len(s)):     # Starting a loop 
        #     count=0                  # setting count to zero because we are starting from new element all the time
        #     hashset=set()             # create a hashset to keep track of duplicates
        #     for j in range(i, len(s)):  # j exactly startas from i and goes till end

        #         if s[j] not in hashset: # check if current element is not in set: if not then: increasse count: update max
        #             count+=1
        #             maxi=max(maxi, count)
        #         else:           # if the element is in the set that means you found duplicate, break and start from next 
        #             break
        # return maxi


        """
        Sliding window
        """

        # left=0
        # res=0
        # hashset=set()                               
        # for right in range(len(s)):       # run a loop till end
        #     while s[right] in hashset:     # while will conitnue check if the duplicate is present in hahset and remove it. if will only check 1 duplicate value if many are present

        #         hashset.remove(s[left])    # telling the set to remove the element that matches the value of s[left]: basically telling set to remove duplicate element from it
        #         left+=1


        #     hashset.add(s[right])         # if not in hashset it will add in hashset 
        #     res =max(res,right - left +1) # calcualte max

        # return res




        








