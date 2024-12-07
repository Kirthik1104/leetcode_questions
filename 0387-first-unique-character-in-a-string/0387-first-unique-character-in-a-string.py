class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}

        for index, char in enumerate(s):
            if char in hashmap:
                hashmap[char][0]+=1
            else:
                hashmap[char]=[1, index]

        for char in hashmap:
            if hashmap[char][0]==1:
                return hashmap[char][1]
        return -1

        # for val in hashmap[char][index]:
        #     print(val)

        