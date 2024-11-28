class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1]*n   # [1,1,1,1]
        right=[1]*n  # [1,1,1,1]
        left_product=1
        right_product=1
        for i in range(len(nums)):
            
            
            left[i]=left_product   # Filling the elements from left to right
            left_product*=nums[i]   # calcualting the current product to left which will be inserted in the next pos
            
            j=-i-1     # starts from reverse to start if i is 0, j is -0-1 which is -1 then -2, -3, -4
            right[j]=right_product # Filling the elements from right to left
            right_product*=nums[j]  # Calculating the current product to right which will be inserted in next pos
            
            
        return ([l*r for l,r in zip(left, right)])  # returning new list by mult both values from left and right



        """
        tIME COMEPLEXITY: o(N)

        """