from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_range(speed: int)->bool:
            times=0
            for pile in piles:
                times+=ceil(pile/speed)
            return times<=h

        
        low = 1
        high = max(piles)
        result = high
        while low<=high:
            mid = (low + high)//2
            if time_range(mid):
                result=mid
                high = mid - 1
            else:
                low = mid + 1
        return result