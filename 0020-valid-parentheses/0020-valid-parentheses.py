class Solution:
    def isValid(self, s: str) -> bool:
        
        # Tc: O(n)
        symbol={")":"(", "}":"{", "]":"["}
        stack=[]

        for char in s:
            if char in symbol: # Check if char is closing brackeet (present as keys in dict). If not closing add in stack
                if stack and stack[-1]==symbol[char]: # if closing bracket. check its coorespong typr and match
                    stack.pop() # if same type and correct fornat. Pop the stack for next type of bracket
                else:
                    return False # Return False immediately if bracket type does not match
            else:
                stack.append(char)

        if not stack:   # if after traversing  stack is empty that means all types of bracket are correct and same. return true
            return True
        else:
            return False # else false









        """
        Stack method

Final Time Complexity
Since the loop iterates through the string once and each stack operation (push and pop) takes constant time, the overall time complexity of the function is:
\U0001d442(\U0001d45b)


        # """
        # stack=[]
        # hashmap={"}":"{", ")":"(", "]":"["}

        # for c in s:
        #     if c in hashmap:  # This conditions check the keys which are the closing brackets, if they are present in dict
        #         # print(c)

        #       # If yes, then we will check if stack is empty ot not with (if empty) and
        #       # Compare the top element, any opening bracket woth its corresponding closing bracket, how?
        #       #  stack[-1] will show the top elememet (bracket) and will check with hashmap[c]:-which is the value    associated with with the corresponding closing bracket or key.
                
        #         if stack and stack[-1]==hashmap[c]: 
        #             stack.pop()             # if same we will pop the top element from stack
        #         else:
        #             return False            # if opening bracket abd closing bracket are not same. we will immedeialty return false

        #     # If stack is empty insert the element        
        #     else:                     
        #         stack.append(c)
        
        # return not stack  # if stack returns true when not empty. and false when empty:--So we will say not empty to make it return true for empty stack


        # """

        # Two pointer method: Not efficent with for mismatched pairs

        # """

        # balance=0

        # for i in s:

        #     if i in "({[":
        #         balance+=1
        #     else:
        #         balance-=1
        #     if balance<0:
        #         return False
            
        # return balance==0




