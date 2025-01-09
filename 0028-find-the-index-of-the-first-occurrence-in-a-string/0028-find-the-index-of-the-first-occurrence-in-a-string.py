class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        m=len(needle)

        left=0
        right=len(needle)

        while right<=len(haystack):  #why =?: for char with length of 1
            if not haystack[left:right].startswith(needle):
                left+=1
                right+=1
            else:
                return left
        return -1














        # m=len(haystack)               # Length og haystack
        # n=len(needle)                 # Length of needle
        # left=0                        # left pointer used to iterate over haystack
        # right=len(needle)             # right pointer (actual length of needle)

        # """
        # Creating a slicing or window of size needle. left=0 and right would be length of needle
        # haystack = "sadbutsad", needle = "sad"

        # left=0
        # right=len(needle)=3

        # - using the window size of needle to check in haystack
        # haystack[left:right] gives haystack[0:3]-->sad.starswith(needle)--> True
        # - if the window size of haystack does not contain string in needle, go to next window by incrementing left and right and checking again

        # - If the window size is found return the left pointer which will give the index of the first occurence of string

        # - else -1

        # """

        # while right<=len(haystack):
        #     if not haystack[left:right].startswith(needle):
        #         left+=1
        #         right+=1
        #     else:
        #         return left
        # return -1
        