class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        Using Bucket fill logic (optiaml)-->without sorting
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
        Using heap (more optiaml than sorting slightly less than bucket fill logic)-->without sorting
        ----------------------
     Time Complexity:
     1)  Building the frequency map:
            Iterating through n elements in the input list to calculate frequencies.
            Time Complexity: O(n)
            
    2) Heap operations for the top k elements:
            Insertions or replacements in the heap take O(log k) per element.
            We process all n elements, performing O(log k) operations for each.
            Time Complexity: O(n log k)
            
    3) Extracting the top k elements:
    
            Once the heap is built, extracting all k elements takes O(k log k).
            However, this step is often dominated by the previous step (O(n log k)), so it is negligible.
            
    4) Total Time Complexity:
            O(n log k)
        """

        import heapq
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        min_heap=[]
        
        for num, count in freq.items():   # get the count associated with the number
            heapq.heappush(min_heap, (count, num))  # In the min_heap store the count with number (count, num). 
            if len(min_heap)>k:                  # if the size of min_heap exceeds length of k heappop removes minimum count and number combination from min heap
                heapq.heappop(min_heap)
        print([num for count, num in min_heap])  # in the end you will the count associated number  inside min_heap












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

       

