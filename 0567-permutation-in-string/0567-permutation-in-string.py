class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2 has premutations of s1 so if s1 lenght is greater than s2 lenght then no premutations can be found in s2. retturn false
        if len(s1)>len(s2):
            return False

        # Get the lenghts of s1 and s2 in n1 and n2 correspondingly
        n1=len(s1)
        n2=len(s2)

        # To store the occurence of chars
        counts1=[0]*26
        counts2=[0]*26
        
        # Creating intial window by traversing n1 length
        for index in range(n1):
            counts1[ord(s1[index]) - ord('a')]+=1 # Stroring length of chars of s1 in counts1
            counts2[ord(s2[index]) - ord('a')]+=1 # Using the same lenght, strong the chars of s2 in counts1]2 (Actual Window)

        if counts1==counts2: # if count is same, return true, else start traversing the window
            return True
            # print(counts1)

        # We have already created the window based on n1 length in counts2
        for i in range(n1, n2): # From window length created in counts2 till end, we will slide exactly by adding:
            char_new=s2[i]        # current element to the counts2 and
            char_removed=s2[i-n1]  # Removing the left mosst element from counts2 (slidng window by adding last and remov from first)

            counts2[ord(char_new)-ord('a')]+=1  # Add the new character at the correct location in counts2 array
            counts2[ord(char_removed)-ord('a')]-=1 # after adding remove the element from left

            if counts1==counts2: # check if after adding and removing the all ones are same as present in counts2 and counts1
                return True  # Return True
        return False # else false
