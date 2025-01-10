class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        start=strs[0]

        for char in strs:
            while not char.startswith(start):
                start=start[:-1]
        return start















        # """
        # 1) Step 1: Take the first string inside a prefix : strs[0]

        # 2) Step 2: Run a for loop from index 1 till end of len of strs.  excluding the prefix index 0 

        # 3) Step 3: store all the words starting from index 1 in a variable called current_word

        # 4) Step 4: Check if current word starts with prefix:

        #     Eg: flower startswith fl or flo or flow-->True) because fl, flo and flow are string less than flower and has same char
        #     Eg1: fl starts with flower -->(False) because fl cannot with flower because flower is bigger than fl--> for fl to start with flowe, we hvae to reduce the flower string to match string fl

        #     by doing prefix=prefix[-1]

        # 5) After reducing flower to fl, fl=fl true, use current word to compare with the new prefix which is fl and repeat same step
       
        # 6)  If after reducing prefix it become "" return immediately
        # """
        # prefix=strs[0]

        # for i in range(1, len(strs)):
        #     current_word=strs[i]

        #     while current_word.startswith(prefix)==False:
        #         prefix=prefix[:-1]

        #         if prefix=="":
        #             return ""
        # return prefix
        """
         strs = ["flower","flow","flight"]

        prefix=flower

        current_word = flow 

        1)  Current_word = flow, prefix =flower 
            flow startswith flower=False (reduce flower, flowe, flow, flo)
                exit while
        2) Current_word  = flight, prefix= fl
                exit while
        return fl

        Tc:O(n): when all  words are same, it wont go inside while

        O(m*n)-->n is length of string, m is no. of comparision

        """
