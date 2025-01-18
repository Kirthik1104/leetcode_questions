class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Tc: O(n)
        1) i and j will both start at same position
        2) for contigous same elements we will keep updating j
        3) If numbers are different then at next position of i (i+1) we will update it with number at j
        4) increment i 
        5) j will keep incrementing till it reaches the end
        6) since we are starting from 0, i+1, returns the correct unique elements
        """

        i=0
        j=0

        while j<len(nums): 
            if nums[i]!=nums[j]:# if number are not eequal
                nums[i+1]=nums[j]
                i+=1
            j+=1       
        return i+1






















        """
        1) j: will start from second index
        2) i: will also start from second index

        Eg:1
        k=1
        for loop i=1
        [1,2,3,4]:
        index 1!=index 0
        2!=1 
        nums[k] which is 1 is equal to nums[i] whichs is also 1, so same value 

        nums[k] which is 2

        """
        j=1                                 # Pointer to keep the index of second duplicate till we find the unique element
        for i in range(1, len(nums)):
            if nums[i]!=nums[i-1]:              # check i with 0
                nums[j]=nums[i]          # update the pointer with unique elements
                j+=1                     # increment pinter
        return j                       # return j

        