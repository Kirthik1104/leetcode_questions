class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        k=k%len(nums)
        self.reverse(nums, 0, len(nums)-1) # reversing from start to end
        self.reverse(nums, 0, k-1)         # Reversing from start to k-1
        self.reverse(nums, k, len(nums)-1) # Reversing from k to end

        return nums
    

    def reverse(self, nums, start, end): #Reversal Logic

        while start<=end:
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
        return nums




















#         """
#         Do not return anything, modify nums in-place instead.

#         Process:
#         Calculate Effective Rotations:k=k%len(nums)=12%5=2
#         Reasoning:A full rotation happens every len(nums)=5 steps.
#         12 steps include:2 full rotations (2×5=10).
#         2 extra steps.
#         Thus, 12 steps are equivalent to rotating 2 steps to the right.
#         """
#         k=k%len(nums)  #--> if ks is greater than len of nums...just consider the remainder and rotate by that,
#         self.reverse(nums, 0, len(nums)-1)  # Reverse whole array
#         self.reverse(nums, 0, k-1)        #  Reverse from start to k
#         self.reverse(nums, k, len(nums)-1)  # reverse from k to end

#         return nums


#     def reverse(self, nums, start, end): # Swapping code to swap the numbers
#         while start<=end:
#             temp=nums[start]
#             nums[start]=nums[end]
#             nums[end]=temp
#             start+=1
#             end-=1
#         return nums

   

        