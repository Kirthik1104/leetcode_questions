class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Tc: O(n)
        """
        gas=0

        for num in nums:
            if gas<0:
                return False
            if num>gas:
                gas=num
            gas-=1
        return True
        