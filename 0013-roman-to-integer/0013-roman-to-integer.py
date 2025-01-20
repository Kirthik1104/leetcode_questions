class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Tc: O(n)
        """
        hashmap={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        result=0

        i=0  # starts from first index
        j=1  # starts from second index
        val=0 # to calculate or set the values during each conditions
        while j<len(s):

            if hashmap[s[j]]>hashmap[s[i]]:  # for IV, IX OR--->for all roman pairs whoes element at first place is smaller than element at second place, than second - last
                val= hashmap[s[j]] - hashmap[s[i]]  # element at second index - element at first index
                result+=val                         # updating the result with val
                i+=2                                # why do we do i+=2 and j+=2 ---> to leave the current pair and go to next pair
                j+=2                                
                val=0                             # reset the val to 0 for next pair or singular value

            elif hashmap[s[j]]>hashmap[s[i]]:     # if elements at adjacent places are equal, do the same step as above, since its a valid pair, skip both indices
                val=hashmap[s[j]] + hashmap[s[i]]
                result+=val
                val=0
                i+=2
                j+=2

            else:                               # if neither iof above conditions--> adjacent pairs are not equal and second element at first is larger than second
                result+=hashmap[s[i]]         # just the add the value in that case
                i+=1                          # since its a single element we would shift i and j by 1 place only
                j+=1

        # this is the case when j exceeded the length of the array but i is still at last position, then add the only element i, because rest would have been pairs or single
        if i<len(s):
            result+=hashmap[s[i]]
        return result
