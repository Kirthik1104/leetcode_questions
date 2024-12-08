class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = m - 1  # Last valid index in nums1
        l2 = n - 1  # Last valid index in nums2
        pointer = m + n - 1  # Last index in nums1

        """
         nums1 = [1,2,3,0,0,0]
         nums2 = [2,5,6]
         Compares the elementt 3 (m-1) last element of nums1 and 6 (n-1) last element of nums2. Places the larger element at end and decrements the index in either one and decrements pinter all the time

         since we are starting the index of nums1 and nums2 from length of m and n and coming backwards the while loop exits case would be if l1 and l2 goes negative
        """
        while l1 >= 0 and l2 >= 0:  # Use and to ensure both are valid
            if nums1[l1] > nums2[l2]:
                nums1[pointer] = nums1[l1]
                l1 -= 1
            else:
                nums1[pointer] = nums2[l2]
                l2 -= 1
            pointer -= 1

        # Copy any remaining elements from nums2 (if any)

        """
        nums1 = [0, 0, 0] (only placeholders, no valid elements), m = 0 (no valid elements in nums1)
        nums2 = [1, 2, 3] (n = 3)

        Here since m is already 0, l1= m-1 would be negative so this while loop would be skipped and second while loop will handle adding the elements from num2 to nums1

        Or

        when if there's any element left in nums2 which has to be added to nums1 and l2 loop has excited already, then this while will take care of that

        """
        while l2 >= 0:  # Only need to check nums2
            nums1[pointer] = nums2[l2]
            l2 -= 1
            pointer -= 1