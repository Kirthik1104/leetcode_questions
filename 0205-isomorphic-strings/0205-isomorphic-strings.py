from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #why? 200 ---> maximum ASCII value for characters (including letters and punctuation marks) is 127. bit extended ASCII values we took a safer length of 200
        array_s=[0]*200  
        array_t=[0]*200

        length_s=len(s)
        length_t=len(t)

        if length_s!=length_t:
            return False


        for i in range(length_s):
            if array_s[ord(s[i])]!=array_t[ord(t[i])]:
                return False


            array_s[ord(s[i])]=i+1
            array_t[ord(t[i])]=i+1
        
        return True

