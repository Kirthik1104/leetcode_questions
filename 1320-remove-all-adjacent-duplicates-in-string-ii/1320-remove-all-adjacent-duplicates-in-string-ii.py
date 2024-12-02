class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        count=1
        for index, char in enumerate(s):
            if stack and char == stack[-1][0]:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([char, count])
        
        res=""
        for char, times in stack:
            res+=char * times
        return res

        