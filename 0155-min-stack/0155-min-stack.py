class MinStack:
    """
    Ecery operation is O(1)
    """
    def __init__(self):
        self.stack=[]
        self.minstack=[]  # Created a stack to keep track of minimum in the main stack (self.stack)
        

    def push(self, val: int) -> None:
        self.stack.append(val) # Upon push method insert element into self.stack

        """
        1) Intially when push method is called, if not self.minstack is executed (when stack is empty, min gets the val assigned)

        2) From second call onwards, if not self.minstack is not executed (because stack is not empty now) the or condition is executed to store only the min. Compares the last val present in minstack with new val if new val is less than append new else minstack will not get new val and will have the existing val as minimum 
        """
        if not self.minstack or val<=self.minstack[-1]: 
            self.minstack.append(val)

        """
        1) if self.stack: # To check if stack has values
        2) if self.stack[-1]==self.minstack[-1]: # Before removing check if the last val in main stack and in minstack is 
        same. if same then remove it from both, so that minstack corectly cooresponds with minimum value from the main stack
        """
    def pop(self) -> None:
        if self.stack: # To check if stack has values
            if self.stack[-1]==self.minstack[-1]: # Before removing check if the last val in main stack and in minstack is same
                self.minstack.pop() # remove it from minstack and from main stack below
            self.stack.pop() # irrespective if present in minstack or not, remove it from main stack

    def top(self) -> int: # to return top element present in stack
        if self.stack:  # check if stack has elements, if yes, 
            return self.stack[-1] # then return the top element present in stack
        

    def getMin(self) -> int:
        if self.minstack: # Check if self.minstack has values, if yes,
            return self.minstack[-1] # then return the top element present in stack
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()