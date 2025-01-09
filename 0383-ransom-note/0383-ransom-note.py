class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashzine={}

        """
        Step 1) Create a hashmap to store the chars of magazine with the count of its occurence. This will be later on used to map the count in ransomNote 
        """
        for char in magazine:
            hashzine[char]=hashzine.get(char, 0)+1 
        """
        Step 2) Now loop the chars in ransomNote, and 
            a) check first condition: if the char in ranso.... and not in maga... --> return False
                a.1)  If char exits in ransom... and in maga...
                        update the count or occurence in hashmap by decrementing by -1
                        check if the value goes below 0, that means the charcter does not match in either strings
            If the loop ran till last that means their exits a match 
        """
        for char in ransomNote:
            if char in hashzine:
                hashzine[char]-=1 # if char in hashzine, decrement count by -1
                if hashzine[char]==-1: # quikcly check if the value is less than 0 if yes, the return False
                    return False
            else:                  # if char exits in ransomNote and does not appears in magazine, return False
                return False
        return True   # If traversed fully that means the patterns are matching
















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
        