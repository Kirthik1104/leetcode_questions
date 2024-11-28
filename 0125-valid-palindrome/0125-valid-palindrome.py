class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=""
        for char in s:
            #Checking if char lies in a-z or A-Z or 0-9, eventually excluding spaces and special character
            if('a'<=char<='z') or ('A'<=char<='Z') or ('0'<=char<='9'):
                result+=char #this result only contains chars without any extra spaces and special characters
        
        #Starting a two pointer approach
        l=0              #Start from left
        r=len(result)-1  #Starts from right
        while l<r:
            if result[l].lower()!=result[r].lower(): #if any of the value are not same, return False immediately
                return False
            l+=1
            r-=1
        return True # If after traversing all values are same return True

        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """


        """
        Avoiding Space complexity by changiing the main string. So Only Tc O(n)
        """
        l=0
        r=len(s)-1

        while l<r:
            # Check if l<r and if not a-z, A-Z, 0-9, thats means its a special character, so we move ahead/skip the index 
            while l<r and not (('a'<=s<='z') or ('A'<=s<='Z') or ('0'<=s<='9')):
                l+=1

            # Check if l<r and if not a-z, A-Z, 0-9, thats means its a special character, so we move back/skip the index 
            while l<r and not (('a'<=s<='z') or ('A'<=s<='Z') or ('0'<=s<='9')):
                r-=1
            
            if s[l].lower()!=s[r].lower(): #if char is not equal, return False
                return False
            l+=1
            r-=1
        return True #if the while loop has traversed fully then it means everything is correct, return true

        
