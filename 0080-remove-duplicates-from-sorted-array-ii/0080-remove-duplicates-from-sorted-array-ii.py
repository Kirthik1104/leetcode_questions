class Solution:
    def removeDuplicates(self, nums:[list])->int:
        """
        1) count is initalised to 1
        i and j are also intitalised to 1 because the first number will always be valid

        step 1: To check if nums at i is equal to i-1, if yes then increase the occurence count, you have to include occurence count in the result till it<=2
        step 2: j pointer: Tracks where the next valid element should be written
        step 3: increment j till occurence lount is less than 2 and it count increases then the if condition will avoid including that number.

        """
        occurence=1
        i=1
        j=1
        for i in range(1, len(nums)): # c
            if nums[i]==nums[i-1]:
                occurence+=1
            else:
                occurence=1
            

            if occurence<=2:
                nums[j]=nums[i]
                j+=1
            
        return j
       



