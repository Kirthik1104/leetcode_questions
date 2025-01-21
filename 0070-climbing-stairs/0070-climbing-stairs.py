class Solution:
    def climbStairs(self, n: int) -> int:
        # Used for memoization, so that if we encounter same values, acces from this dictionary

        """
        why 1, 2 and not 0, 1---> To reach step 1 we need 1 step or way, to reach step 2, we can directly go to step 2 or go 1+1step. basically finding n ways to reach a step
        
        And anything greater than 2--> we will start exploring the permutation from their and store the results in hashmap

        when 1 and 2 are in memo
        when n=2 the answer should be 2---> 1+1 or directly 2, read description

        if only 1 and 0 are in memo,
        then n=2 will give 1--> which is wrong as per description

        Tc: O(n)
        """
        memo={1:1, 2:2} 
        # And frp,

        def fib(x):
            if x in memo:
                return memo[x]
            
            memo[x]= fib(x-1) + fib(x-2)
            return memo[x]

        return fib(n)