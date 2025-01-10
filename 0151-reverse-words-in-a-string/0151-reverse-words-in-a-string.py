class Solution:
    def reverseWords(self, s: str) -> str:
        res=s.strip()
        left=len(res)-1
        right=len(res)
        result=[]

        while left>=0:
            if res[left]==" ":
                
                if left+1!= right:
                    result.append(res[left+1: right])
                right=left
            left-=1
        result.append(res[left+1:right])

        return " ".join(result)















        # i, j, result=0,0, ""
        # n=len(s)
        # while i<n:
        #     while i<n and s[i]==" ":
        #         i+=1
        #     if i>=n:
        #         break
        #     j=i+1
        #     while j<n and s[j]!=" ":
        #         j+=1
        #     sub=s[i:j]

        #     if len(result)== 0:
        #         result=sub
        #     else:
        #         result=sub+" "+result
        #     i=j
        # return result
        