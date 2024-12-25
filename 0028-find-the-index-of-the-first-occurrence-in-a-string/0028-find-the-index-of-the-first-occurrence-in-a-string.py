class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m=len(haystack)
        n=len(needle)
        left=0
        right=len(needle)

        while right<=len(haystack):
            if not haystack[left:right].startswith(needle):
                left+=1
                right+=1
            else:
                return left
        return -1
        