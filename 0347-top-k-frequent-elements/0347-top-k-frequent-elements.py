class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        Using Bucket fill logic (optiaml)-->without soring
        ----------------------
        Short Summary
        Time Complexity: O(n)
        Constructing the hashmap: O(n)
        Filling the buckets: O(n)
        Collecting results: O(n)

        Space Complexity: O(n)
        Hashmap: O(n)
        Buckets: O(n)
        Result list: O(k), where k≤n.
        """
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


















        """
        Using hashing and sorting (not optimal)->invoves sorting
        ------------------------
        Time Complexity:

        Your Code: 

        O(n+mlogm) or O(nlogn).
        # """
        # freq={}
        # for i in nums:
        #     if i not in freq:
        #         freq[i]=1
        #     else:
        #         freq[i]+=1

        # sorted_freq=sorted(freq.items(), key=lambda item:item[1], reverse=True) #sorted returns tuple
        
        # res=[]
        # for i in range(k):   # since we got values in descending order. we got top k elemnents
        #     res.append(sorted_freq[i][0])  #[positon][value from that psotion]
        # return res

       

