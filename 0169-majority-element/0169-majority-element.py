class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}

        for num in nums:
            hashmap[num]=hashmap.get(num, 0)+1
        
        for key, val in hashmap.items():
            if val>len(nums)//2:
                return key 



























        # n = len(nums)
        # cnt = 0  # Count
        # el = None  # Element

        # # Applying the algorithm
        # for i in range(n):
        #     if cnt == 0:
        #         cnt = 1
        #         el = nums[i]
        #     elif el == nums[i]:
        #         cnt += 1
        #     else:
        #         cnt -= 1

        # # Checking if the stored element is the majority element
        # cnt1 = 0
        # for i in range(n):
        #     if nums[i] == el:
        #         cnt1 += 1

        # if cnt1 > (n / 2):
        #     return el
        # return -1







        # freq={}
        # n=len(nums)
        # for num in nums:
        #         freq[num]=freq.get(num,0)+1

        # for i in freq:
        #     if freq[i]>n//2:
        #         return i

        # n=len(nums)

        # for i in range(n):
        #     count=0
        #     for j in range(n):
        #         if nums[i]==nums[j]:
        #             count+=1 
        #     if count> n/2:
        #         return nums[i]
