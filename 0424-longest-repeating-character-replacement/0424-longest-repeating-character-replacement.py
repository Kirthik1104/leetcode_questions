class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        """
        Tc: O(n)
        Sc: O(n)

        1) right-left+1 - max(count.values())-->calculates the number of characters in the current window that are not the most frequent character. 

        2)how?? at a length 5 the most freq character is 3, so 5-3 gives no. of characters
that are not most frequent, which can be changed, but should fall under or equal to the no of swaps allowed (<=k)

        3) right-left+1 - max(count.values()) : Gives less frequnet characters which can be converted to create a uniform characters, if it EXCEEDS k:
        
        4) we have to shrink the window by increm.. left by 1 and if window is shrinked then count of a char should be decreased from count dict as well, because if window size is reduced then a count of char will also be lost

            4.1) Decrrement the count: get the first char(initally) which left points to s[left] and decremting its count from count dict
            4.2) After that Shrink the window size by incrementing the left by 1
        """
        left=0
        res=0
        count={}
        for right in range(len(s)):
            count[s[right]]=count.get(s[right], 0)+1
            
            # No. of less frequent elemt = length - Count of max frequen elemt. if greater than k,
            if right-left+1 - max(count.values())>k:
                count[s[left]]-=1 # To shrink, first decrease count dict and then
                left+=1            # to actually shrink, increase the left by 1
            
            res=max(res, right-left+1)  # Will calculate the max of longest repeating characters. Left will be updated from above if its not in bound with k swaps
        return res
        