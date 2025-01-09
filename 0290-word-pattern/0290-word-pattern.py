from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split(' ')
        hashmap={}
        if len(pattern)!=len(word):
            return False
        
       #set will give pattern as 'a' and keep dog and cat as  and their is not equal
        
        if len(set(pattern))!=len(set(word)): 
            return False
        
        for ind in range(len(pattern)):
            if pattern[ind] not in hashmap:
                hashmap[pattern[ind]] = word[ind]
                
            elif hashmap[pattern[ind]]!=word[ind]:
              
                return False
        return True











        """
        Space: O(n) - scan
        Time: O(n) - for the hashmap

        """
        new_words=s.split(' ')  #----> Converting string of words to list of words

        if len(pattern)!=len(new_words):   # if length of pattern and length of new_words does not match return False
            return False
        
        """
        pattern="aa"
        s="dog, cat"

        set will give pattern as 'a' and keep dog and cat as  and their is not equal
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

        


            