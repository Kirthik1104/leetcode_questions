class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set()
        for i in nums:
            hashset.add(i)
        maxi=0
        for i in nums:
            if i-1 not in hashset:
                val=i
                count=0
                while val in hashset:
                    val+=1
                    count+=1
                maxi=max(maxi, count)
                    # print(maxi)
        return maxi


























#         """
# Overall Time Complexity
# -----------------------------
# The overall time complexity of the algorithm can be expressed as:
# O(n) for building the hashset
# O(n) for iterating through nums
# O(k) for the inner while loop, where k is the total count of unique consecutive numbers processed.
# Since each number is effectively processed once, the total operations will sum up to O(n) for both loops, resulting in an overall time complexity of O(n).
#         """
#         if len(nums)==0:    # if nums is [] or [0] return 0
#             return 0

#         hashset=set()       # Below three line: Traverse and store all the values in a set
#         for number in nums:
#             hashset.add(number)
        
        
#         maxi=1               # to keep track of max values

#         for i in nums:        # access each element

#             if i-1 not in hashset:   # check if i-1 not in hashset---> This means i is the starting number of sequnce
#                 start_value=i      # value to store the start value
#                 count=1            # to keep count of occuerence
#                 while start_value + count in hashset: # cheeck if next number in hashset: yes then add and increment count
#                     count+=1
#                 maxi=max(maxi, count)  # if next number not present update the maxi
#         return maxi
        


#         """
#         Overall Time Complexity: The overall time complexity of the algorithm is dominated by the sorting step, resulting in O(n log n)
#         """
#         # if len(nums)==0:
#         #     return 0
#         # nums.sort()


#         # maxi=1
#         # n=len(nums)   # sort the arry to get  [1,2,3,4,100]
#         # count=1
#         # for i in range(1,n):      # start the loop froom and compares its previous value. if its same

#         #     if nums[i]==nums[i-1]:
#         #         continue # if the cuurent element is equal to previous element, go to next iteration and skip below

#         #     if nums[i]==nums[i-1]+1:    # if value at i same as i-1+1. increment count
#         #         count+=1
#         #     else:
#         #         maxi=max(maxi, count)   # Sequence has stopped so update the count with maxi
#         #         count=1    # set the count back to 1 again so that it starts fresh from next itreraiton

#         # maxi = max(maxi, count)   # after the final sequence checck again
#         # return maxi
