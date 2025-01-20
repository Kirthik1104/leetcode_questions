class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        1) far is the distance (index + element at that index) whihc is used to move ahead in array
        2) The problem gurantess a solution--> so we somehow need to get the index where we are jumping to, thats why we are adding index + element at that 
        index

        3)  so far, we can also say it as jump, travels forward in array
        [2,3,1,1,4]
        --> first iteration far is set to 0+2 = 2nd index, jump is updated to 1, end is also updated to far

        --> second iteration, far is set to 1+3 = 4th index, jumps is not updaed yet why---> becaue i has not reached the end yet

        end is the end or last position of current jump, so end is at index 2, and i is at index 1,still have to reach index 2 to complete the first jump

        4) as we reach index 2 end is updated to far which is index 4 (3+1)= 4

        5) why stop at n-1 (second last index)--> because we dont have to jump from last index, and last index is destination, so thats why we stop at second last index. And just think by the time we reach second last index we know if we can reach last index or not, because the far index would be already updated
        before reaching second last index or at second last index 

        6) would also work for this test case [1,2]--> n-1 means second last index, for first jump will always be i==end, so jump=1
        """
        far=0
        end=0
        n=len(nums)
        jump=0
        for i in range(n-1):
            far=max(far, i+nums[i])
            
            if i==end:
                end=far
                jump+=1

        return jump


        """
        For nums = [2, 0, 0, 1, 4], it is impossible to reach the last index. This violates the problem's guarantee that a solution exists. If this input
        were valid, it would represent an edge case the algorithm is designed to handle gracefully.
        """