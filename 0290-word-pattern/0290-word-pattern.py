from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new_words=s.split(' ')  #----> Converting string of words to list of words

        if len(pattern)!=len(new_words):   # if length of pattern and length of new_words does not match return False
            return False
        
        """
        pattern="aa"
        s="dog, cat"

        set will give pattern as 'a' and keep dog and cat as as and their is not equal
        """
        if len(set(pattern))!=len(set(new_words)): 
            return False
        
        hashmap={}

        for index in range(len(pattern)):
            if pattern[index] not in hashmap:
                hashmap[pattern[index]] = new_words[index]
            elif hashmap[pattern[index]]!= new_words[index]:
                return False
        
        return True

        


            