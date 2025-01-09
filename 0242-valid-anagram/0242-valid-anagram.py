class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        hashmap={}
        #---> The total time complexity for this loop is O(n)
        for char1, char2 in zip(s, t):                  #---> O(n) because 1 for loop is used
            hashmap[char1]=hashmap.get(char1, 0)+1      #---> dictionary operations: which are O(1) operations on average.
            hashmap[char2]=hashmap.get(char2, 0)-1
 
        # For English lowercase letters, the number of unique characters is 26, but this is a constant.     
        # Since the number of unique characters is small and constant, this loop runs in O(k) time, where k is a constant (at most 26).  
        #-->Thus, the total time complexity is O(n + k), which simplifies to O(n) since k is constant (26 at most).
        for value in hashmap.values():
            if value!=0:
                return False
        return True
        """
        Space Complexity
        ---------------
        --->In the worst case, the hashmap will have an entry for every unique character in both strings. Since we're considering lowercase English letters, the maximum
        number of unique characters is 26.
        --->Therefore, the space complexity for the hashmap is O(k), where k is the number of unique characters. As k is constant (26), this simplifies to O(1) space.
        """
 

        


















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
            
