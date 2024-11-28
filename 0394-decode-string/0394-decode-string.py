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