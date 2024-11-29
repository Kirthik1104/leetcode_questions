class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        """
        Time complexity: O(n)

        Since array is already sorted then we no need to create a dic to store the index and val, we can directly use two pointer

        """
        left=0
        right=len(numbers)-1

        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left+1, right+1]
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                left+=1
        