class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]

            if remaining is "":
                return [""]


            result=[]
            for i in range(1, len(remaining)+1):
                prefix=remaining[:i]
                if prefix in wordDict:
                    sufix=dfs(remaining[i:])

                    for sentence in sufix:
                        if sentence:
                            result.append(prefix+ " "+ sentence)
                        else:
                            result.append(prefix)

            memo[remaining]=result
            return result
        
        memo={}
        return dfs(s)
        