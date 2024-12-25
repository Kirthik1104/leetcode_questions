class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
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

        