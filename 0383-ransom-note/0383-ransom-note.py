class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashzine={}

        for char in magazine:
            hashzine[char]=hashzine.get(char, 0)+1
        print(hashzine)
        for char in ransomNote:
            if char in hashzine:
                hashzine[char]-=1
                if hashzine[char]==-1:
                    return False
            else:
                return False
        return True
















        # hashmap1={}
        # hashmap2={}
        # for char in magazine:
        #     hashmap1[char]=hashmap1.get(char, 0)+1

        # for char in ransomNote:
        #     if char in hashmap1:
        #         hashmap1[char]-=1
        #         if hashmap1[char]==-1:
        #             return False
        #     else:
        #         return False
        # return True
        