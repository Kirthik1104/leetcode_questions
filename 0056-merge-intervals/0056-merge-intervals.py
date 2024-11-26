class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]

        #Sorting based on 1st elementt of every sub array
        #for interval in sorted(intervals, key=lambda x:x[0]):


        """
        why the above for loop for sorting is necessary
        Example: Consider intervals like [[5, 6], [1, 3], [2, 4]]. If we process  these in the original order:
        --When examining [5, 6], there's no overlap with [1, 3], so we add it to res.
        --When examining [1, 3], we add it to res.
        --Finally, when checking [2, 4], we see it overlaps with [1, 3], so we merge them. But since we didn’t have a sorted order initially, we might not recognize overlaps optimally for all pairs.

        Solution better to sort: Using 1st element 
        ------------------------------------------
        """

        for interval in sorted(intervals, key=lambda x:x[0]):   #Takes individual sub array

    
    # 1---------------3  (res=[1,3]: Already inside of stack)
    #      2---------------6
 #[2,6]   #interval[0] :checks first element of current sub array ([2, 6]) : 2 
 #[1,3]  #res[-1][1]: [-1]from last sub array from res stack. [1] second elemet of it: 3:     2<=3

            if res and interval[0]<=res[-1][1]: 

    # 1------------3
    #     2--------------6
                
                """
                [-1]: [1,3]: Gives Last position from stack
                [1]: [3]: updating 1st position with
                
                Interval = [2,6] , res =[1,3]
                max(interval[1] :--6)
                                    ====6
                max(res[-1][1]:---3)


                """   
                res[-1][1]=max(interval[1], res[-1][1])

            
            else:
                res.append(interval) # inserts 1st sub array into stack
        return res

"""
Time Complexity of Your Code
The original code provided has the following time complexities:

Sorting the Intervals: O(nlogn) : The intervals are sorted based on their start times.
-------------------------------

Merging Intervals: O(n): We traverse the sorted list of intervals once to merge them.
-------------------------

Overall Time Complexity: The total time complexity is dominated by the sorting step, which results in O(nlogn).

"""



"""
Summary
-----------
In essence, your solution effectively applies a greedy strategy by making a series of local decisions (merging intervals when possible) based on the current state of the solution. This leads to a globally optimal solution for the merging intervals problem, making it a classic example of the greedy algorithm paradigm.

"""


       
                            