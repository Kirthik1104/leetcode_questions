class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        n1=len(s1)
        n2=len(s2)

        counts1=[0]*26
        counts2=[0]*26

        for index in range(n1):
            counts1[ord(s1[index]) - ord('a')]+=1
            counts2[ord(s2[index]) - ord('a')]+=1

        if counts1==counts2:
            return True
            # print(counts1)

        for i in range(n1, n2):
            char_new=s2[i]
            char_removed=s2[i-n1]

            counts2[ord(char_new)-ord('a')]+=1
            counts2[ord(char_removed)-ord('a')]-=1

            if counts1==counts2:
                return True
        return False
