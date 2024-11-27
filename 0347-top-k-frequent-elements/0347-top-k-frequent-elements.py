class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=[[]for _ in range(len(nums)+1)]
        hashmap={}

        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        for num, freq in hashmap.items():
            count[freq].append(num)
 
        result=[]
        for i in range(len(count)-1, -1, -1):
            for num in count[i]:
                if count[i]:
                    result.append(num)
                    if len(result)==k:
                        return result


















#         """
# Time Complexity:

# Your Code: 

# O(n+mlogm) or O(nlogn).
#         # """
#         # freq={}
#         # for i in nums:
#         #     if i not in freq:
#         #         freq[i]=1
#         #     else:
#         #         freq[i]+=1

#         # sorted_freq=sorted(freq.items(), key=lambda item:item[1], reverse=True) #sorted returns tuple
        
#         # res=[]
#         # for i in range(k):   # since we got values in descending order. we got top k elemnents
#         #     res.append(sorted_freq[i][0])  #[positon][value from that psotion]
#         # return res

       
#        """
#         Hashing


#         Summary
# Time Complexity: O(n)
# Space Complexity: O(n)

# Overall Time Complexity
# Combining these parts, we get:

# Total Time Complexity:
# ----------------------
# The counting and bucket filling steps combined yield ------O(n)+O(m) (or approximately O(n)).
# The final result-building step gives O(n) in the worst case.
# So, the overall time complexity can be approximated as: Overall Time Complexity: O(n)


# Space Complexity
# -------------------
# The space complexity for this solution includes:
# The count dictionary, which can take up to O(m) space.
# The freq list, which can take up to O(n) space for the frequency buckets.
# The res list, which stores the result and can take up to O(k) space.
#        """

   
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]

#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#         for n, c in count.items():
#             freq[c].append(n)

#         res = []
#         for i in range(len(freq) - 1, -1, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res
