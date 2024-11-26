class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap={}

        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        print(hashmap)
        for val in hashmap.values():
            if val>1:
                return True
        return False
        