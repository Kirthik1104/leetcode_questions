class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        for char in s:
            if char not in hashmap:
                hashmap[char]=1
            else:
                hashmap[char]+=1
            
        for char in t:
            if char not in hashmap:
                return False
            else:
                hashmap[char]-=1
        
        for value in hashmap.values():
            if value!=0:
                return False
        return True



















        # # Check if the lengths of the two strings are different
        # # If lengths are not equal, they can't be anagrams
        # if len(s) != len(t):
        #     return False
        
        # # Initialize a hashmap (dictionary) to count character frequencies in string s
        # hashmap = {}

        # # Populate the hashmap with the frequency of each character in string s
        # for letter in s:
        #     if letter in hashmap:
        #         hashmap[letter] += 1  # Increment count if the character exists
        #     else:
        #         hashmap[letter] = 1  # Add the character with count 1 if it doesn't exist
        
        # # Traverse through string t and update the character frequencies in the hashmap
        # for letter in t:
        #     if letter in hashmap:
        #         hashmap[letter] -= 1  # Decrement the count for each character
        #     else:
        #         return False  # If a character in t doesn't exist in hashmap, not anagrams
        
        # # After processing both strings, check if all character counts are zero
        # for char in hashmap:
        #     if hashmap[char] != 0:
        #         return False  # If any count is not zero, s and t are not anagrams

        # # If all counts are zero, return True (strings are anagrams)
        # return True

        # for count1, count2 inz zip(s, t):
            
