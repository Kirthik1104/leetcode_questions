class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
         """
        Overall Time Complexity:
        -----------------------------
        The overall time complexity of the algorithm can be expressed as:
        - O(n) for building the hashset
        - O(n) for iterating through nums
        - O(k) for the inner while loop, where k is the total count of unique consecutive numbers processed.
        Since each number is effectively processed once, the total operations will sum up to O(n) for both loops, resulting in an overall time complexity of O(n).
        """
        if len(nums)==0:    # if nums is [] or [0] return 0
            return 0

        hashset=set()
        for i in nums:
            hashset.add(i)    #adding all the values inside of hashset()
        maxi=0

        for curr_num in nums:      #starting a loop with each number in nums
            if curr_num-1 not in hashset: # Only go inside if curr_num - 1 not in hashset(). If no. is present then curr_num is not starting no.
                val=curr_num   # if there's no element before curr_num then curr_num is starting no. set to val
                count=0        # set count to 0
                while val in hashset:  # start a while loop to check curr_num and consequtive no's
                    val+=1            # update val to next number
                    count+=1          # increment count to signify the sequence
                maxi=max(maxi, count) # if next sequence not present then update the maxi with count
                    
        return maxi





        """
        Overall Time Complexity: The overall time complexity of the algorithm is dominated by the sorting step, resulting in O(n log n)
        """
        if len(nums)==0:
            return 0
        nums.sort()


        maxi=1
        n=len(nums)   # sort the arry to get  [1,2,3,4,100]
        count=1
        for i in range(1,n):      # start the loop froom and compares its previous value. if its same

            if nums[i]==nums[i-1]:
                continue # if the cuurent element is equal to previous element, go to next iteration and skip below

            if nums[i]==nums[i-1]+1:    # if value at i same as i-1+1. increment count
                count+=1
            else:
                maxi=max(maxi, count)   # Sequence has stopped so update the count with maxi
                count=1    # set the count back to 1 again so that it starts fresh from next itreraiton

        maxi = max(maxi, count)   # after the final sequence checck again
        return maxi
