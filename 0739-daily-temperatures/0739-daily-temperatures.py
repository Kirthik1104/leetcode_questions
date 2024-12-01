class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Tc: O(n)
        n=len(temperatures)
        stack=[]
        result=[0]*n

        """
        1) For the first iteration the stack stores in intial temp and its index val,
        2) For second iteration it checks if the temp  at second iteration is > greater than top element present in stack (previous)-> if yes pop the top temp from stack which is lesser than current temp, add the difference to result and add the current temp in stack
        3) If the temp is smaller than previous one add it to stack, because its a monolithic stack, smaller to larger, so if you find a current, smaller one then previous one add it to stack
        """

        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:  # 
                stackt, stacki = stack.pop()
                result[stacki]=i-stacki
            stack.append((t, i))     #
        return result 