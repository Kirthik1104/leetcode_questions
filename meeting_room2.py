from typing import List

def minMeetingRooms(intervals: List[List[int]]) -> bool:
    s = 0  # Pointer for the start times list
    e = 0  # Pointer for the end times list
    count = 0  # Variable to track the current number of overlapping meetings
    res = 0  # Variable to track the maximum number of overlapping meetings (which equals the minimum meeting rooms needed)

    # Sorting the start times and end times from the intervals
    start = sorted([start for start, end in intervals])  # List of start times sorted in ascending order
    end = sorted([end for start, end in intervals])      # List of end times sorted in ascending order

  # Iterate over the intervals using two pointers (s for start, e for end)
    while s < len(intervals):
        if start[s] < end[e]:  # If the next meeting starts before the previous one ends
            count += 1  # Increment the count of overlapping meetings
            s += 1  # Move the pointer for the start times list
          
        else:  # If the next meeting ends before or at the same time the next one starts
            count -= 1  # Decrease the count of overlapping meetings
            e += 1  # Move the pointer for the end times list

        res = max(count, res)  # Keep track of the maximum number of overlapping meetings (rooms required)
    
     # Return the maximum number of rooms needed
    return res
            
            
        
# Test Cases
intervals_0 = [[0, 8],[8, 10]]
intervals_1 = [[0, 30],[5, 10],[15, 20]]  # Expected Output: 2
intervals_2 = [[7, 10], [2, 4]]              # Expected Output: 1
intervals_3 = [[1, 5], [2, 3], [3, 4]]      # Expected Output: 2
intervals_4 = [[1, 2], [2, 3], [3, 4]]      # Expected Output: 1

# Running the test cases
print(minMeetingRooms(intervals_0))
print(minMeetingRooms(intervals_1))  # Output: 2
print(minMeetingRooms(intervals_2))  # Output: 1
print(minMeetingRooms(intervals_3))  # Output: 2
print(minMeetingRooms(intervals_4))  # Output: 1



Time Complexity:
---------------------
Sorting both the start and end times: O(n log n)
Iterating through the lists: O(n)
Overall time complexity: O(n log n) where n is the number of meetings.
  
Space Complexity:
------------------------
O(n) due to the space used by the sorted start and end lists.

###Ouput:
Test Case 1: [[0, 8], [8, 10]]
Sorted Start Times: [0, 8]
Sorted End Times: [8, 10]
Output: 1

Explanation:

Here, there are two meetings: one from 0 to 8 and another from 8 to 10.
The second meeting starts exactly when the first one ends, so there is no overlap.
Since there's no conflict, only 1 room is needed for both meetings.

---------------------------------------------------------

Test Case 2: [[0, 30], [5, 10], [15, 20]]
Sorted Start Times: [0, 5, 15]
Sorted End Times: [10, 20, 30]
Output: 2

Explanation:

The meetings (0, 30) and (5, 10) overlap because the second meeting starts while the first one is still going on. Similarly, (0, 30) and (15, 20) also overlap.
To handle these conflicts, we need 2 rooms: one for (0, 30) and another for (5, 10) or (15, 20).

------------------------------------------------------------------------------------------------
  
Test Case 3: [[7, 10], [2, 4]]
Sorted Start Times: [2, 7]
Sorted End Times: [4, 10]
Output: 1

Explanation:

The two meetings are (7, 10) and (2, 4). The second meeting finishes before the first one starts, so there’s no overlap.
Only 1 room is needed, as both meetings can fit into the same room without any issues.

  ------------------------------------------------------------------------------------------
  
Test Case 4: [[1, 5], [2, 3], [3, 4]]
Sorted Start Times: [1, 2, 3]
Sorted End Times: [3, 4, 5]
Output: 2

Explanation:

Here, the meetings overlap as follows:
(1, 5) overlaps with (2, 3)
(2, 3) overlaps with (3, 4)
In this case, 2 rooms are needed to accommodate all the meetings, as at least two meetings are happening at the same time.

--------------------------------------------------------------------------------------------------
Test Case 5: [[1, 2], [2, 3], [3, 4]]
Sorted Start Times: [1, 2, 3]
Sorted End Times: [2, 3, 4]
Output: 1

Explanation:

The meetings (1, 2), (2, 3), and (3, 4) do not overlap because each meeting ends exactly when the next one starts.
Therefore, only 1 room is needed to accommodate all the meetings.
