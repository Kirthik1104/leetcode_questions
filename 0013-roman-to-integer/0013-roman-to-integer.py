class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        result=0
        i=0
        j=1
        val=0
        while j<len(s):

            if hashmap[s[j]]>hashmap[s[i]]:
                val= hashmap[s[j]] - hashmap[s[i]]
                result+=val
                i+=2
                j+=2
                val=0
            elif hashmap[s[j]]>hashmap[s[i]]:
                val=hashmap[s[j]] + hashmap[s[i]]
                result+=val
                val=0
                i+=2
                j+=2
            else:
                result+=hashmap[s[i]]
                i+=1
                j+=1
        if i<len(s):
            result+=hashmap[s[i]]
        return result
