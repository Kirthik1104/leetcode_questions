class Solution:
    def decodeString(self, s: str) -> str:
        numstack=[]
        strstack=[]
        curnum=0
        curstr=""

        for char in s:
            if char.isdigit():
                curnum=curnum*10 + int(char)
            elif char == '[':                              # Before the opening bracket add all the cur num and curstr to their stack and empty them so that whatever is coming inside this square brackets can be processed further
                numstack.append(curnum)
                strstack.append(curstr)
                curnum=0
                curstr=""
            elif char == ']':                       # Before the closing brackets pop the previous number from stack and store it in times, and pop the previous from strstack and store it in previous and 
                times=numstack.pop() 
                previous=strstack.pop()
                curstr=previous + (curstr*times)    # multiply the current char with previous nums(times
            else:
                curstr+=char
        return curstr

        # Input: s = "3[a]2[bc]"
        # https://imgur.com/kg07U4I

        # Input: s = "3[a2[c]]"
        # https://imgur.com/a/3o489xG
