class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=""
        for char in s:
            if('a'<=char<='z') or ('A'<=char<='Z') or ('0'<=char<='9'):
                result+=char
        l=0
        r=len(result)-1
        while l<r:
            if result[l].lower()!=result[r].lower():
                print(result[l].lower(), result[r].lower())
                return False
            l+=1
            r-=1
        return True 

        