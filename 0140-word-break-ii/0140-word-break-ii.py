class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]

            if remaining is "": #This is the base condition when after slicing all chars there's empty string. Catsanddog. when prefix is dog and sufix is [dog:], there nothing after. python gives "" even if there is nothing after end index of dog.
                return [""] # Why we are returning empty in list. Because for base case we need to append suffx in result and since its empty we have to append in else case, "" will give error so thats why we use [""]

            result=[] # stores the sentence
            for i in range(1, len(remaining)+1):#why start from 1? [:1] cause it access 0th index (n-1).And why len(rem..)-1 because we need to access the last element as well, len(remai) will acces 2nd last, +1 will acces last 
                prefix=remaining[:i] # Gathering prefix (c, ca, cat in worddict in below worddict)-->Access the sufix or the chars after cat and start dfs and repeat same process again
                if prefix in wordDict:
                    sufix=dfs(remaining[i:])

                    for sentence in sufix: #After sufix returns from dfs prefix+suffix is actually the main string (remaining string) for current iteration or call 
                        if sentence:
                            result.append(prefix+ " "+ sentence) # After else, this if condition will run till last
                        else:
                            result.append(prefix)  # else takes first. First prefix insetion because sufix returned "" and prefic would be the last elememt present in worddict

            memo[remaining]=result # memoize the result for current string (remaining) in memoization. so that if same string appears again it can be access from the result stored in memoization (base cond) rather than running dfs again
            return result
        
        memo={}
        return dfs(s)
        

        """
        Formula:
The total time complexity is bounded by:

\U0001d442(\U0001d45b2 ⋅ \U0001d458 + total output size)

Where:

\U0001d45b2: n substrings, each with n prefixes checked.
\U0001d458: Time to look up prefixes in the word set.

total output size: The cost of storing and combining sentences, which depends on the number of valid splits and the length of sentences.

        """