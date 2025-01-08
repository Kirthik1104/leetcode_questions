from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #why? 200 ---> maximum ASCII value for characters (including letters and punctuation marks) is 127. bit extended ASCII values we took a safer length of 200
        array_s=[0]*200  
        array_t=[0]*200

        
        length_s=len(s) 
        length_t=len(t)

        # if the length of t and s are not same then return False
        if length_s!=length_t:
            return False

        """
        for each character go to array and update the count
        for i=0      e                             a
        array_s = [_ 1 _ _ _ _ _ _ _ ]  array_t = [1 _ _ _ _ _ _ _ _ ]

        for i=1      e         g                   a     d
        array_s = [_ 1 _ _ _ _ 2 _ _ ]  array_t = [1 _ _ 2 _ _ _ _ _ ]

        for i=2      e         g                   a     d
        array_s = [_ 1 _ _ _ _ 3 _ _ ]  array_t = [1 _ _ 3 _ _ _ _ _ ]

        since the of g and d are same, it is isomorphic. Update the count
        
        
        
        """
        for i in range(length_s):
            if array_s[ord(s[i])]!=array_t[ord(t[i])]:
                return False


            array_s[ord(s[i])]=i+1
            array_t[ord(t[i])]=i+1
        
        return True


        """

        Final Time Complexity:
        The time complexity for each step:
        ---------------------------------
        Initializing the arrays: O(1)
        Checking the lengths: O(1)
        Iterating over the strings: O(n)

        Sc
        ----
        O(1)
        """
