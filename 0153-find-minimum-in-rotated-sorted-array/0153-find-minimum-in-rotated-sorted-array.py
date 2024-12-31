class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        target=nums[0]

        while low<=high:
            mid = (low + high)//2

            if target < nums[mid]:
                low=mid+1
            if target> nums[mid]:
                target=nums[mid]
                high=mid-1

            else:
                low=mid+1
        return target





























        # low=0
        # n=len(nums)
        # high=n-1
        # target=nums[0]
        # while low<=high:
        #     mid=(low+high)//2

        #     if nums[mid]==target:
        #         return mid
            
        #     if nums[low]<=nums[mid]:
        #         if nums[low]<=target and target<= nums[mid]:
        #             high=mid-1
        #         else:
        #             low=mid+1
        #     else:
        #         if nums[mid]<=target and target<=nums[high]:
        #             low=mid+1
        #         else:
        #             high=mid-1
        # return -1