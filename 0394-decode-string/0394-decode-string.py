class Solution:
    def decodeString(self, s: str) -> str:
        numstack=[]
        strstack=[]
        curnum=0
        curstr=""

        for char in s:
            if char.isdigit():
                curnum=curnum*10 + int(char)
            elif char == '[':
                numstack.append(curnum)
                strstack.append(curstr)
                curnum=0
                curstr=""
            elif char == ']':
                times=numstack.pop()
                previous=strstack.pop()
                curstr=previous + (curstr*times)
            else:
                curstr+=char
        return curstr

        # Input: s = "3[a]2[bc]"
        # https://imgur.com/kg07U4I

        # Input: s = "3[a2[c]]"
        # https://imgur.com/a/3o489xG