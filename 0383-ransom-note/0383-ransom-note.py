class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap1={}
        hashmap2={}
        for char in magazine:
            hashmap1[char]=hashmap1.get(char, 0)+1
        for char in ransomNote:
            hashmap2[char]=hashmap2.get(char, 0)+1
        # print(hashmap1)


        current=True
        for char in ransomNote:
            if char in hashmap1:
                hashmap1[char]-=1
                if hashmap1[char]==-1:
                    return False
            else:
                return False
        return True
        # pointer=0

        # while pointer<len(ransomNote) and pointer<len(magazine):
        #     if ransomNote[pointer]==magazine[pointer]:
        #         pointer+=1
        #     else:
        #         return False
        #     # pointer+=1
        # return True
        
        