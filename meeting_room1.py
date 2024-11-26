# Meeting Room Scheduler

## Problem Description

Given an array of meeting time intervals, each represented by a pair of start and end times `[[start_1, end_1], [start_2, end_2], ...]` (where `start_i < end_i`), determine if a person can add all meetings to their schedule without any conflicts.

Example 1:
Input: intervals = [(0, 30), (5, 10), (15, 20)]
Output: False
Explanation:

The meeting intervals (0,30) and (5,10) will conflict because the meeting that starts at 5 will overlap with the one that ends at 30.
Similarly, the meeting intervals (0,30) and (15,20) will conflict because the meeting that starts at 15 will overlap with the one that ends at 30.


from typing import List

def minMeetingRooms(intervals: List[List[int]]) -> bool:
   

    """
    1) Sort the sub array based on the first element: Using sorted and lambda
    2) Enter the first subarray into the res list
    3) Check if the first element of second sub array is less then the last element of first sub array
       res=[0, 30]
       current interval is [5, 10] 

       interval[0]: 5 (whihc is first element of second subarray)
       res[-1]: returns last subarray from res list [0,30], [1]: returns last element of the from the subarray [30]

    4) Returns false immediately, if theies any conflict. because question is if he can attend all meeting.
    5) Else if all meeting are distant from each other then they he can attend all meeting

       -------------------------------
       0                              30
               ---------------
               5              10

               False as meeting is overlapping


        --------      --------
        0      10     15     20
          True as no overlapping

    Tc: nlogn for sorting
    Space: O(n)
          
    """
    res=[]
    sorted_interval=sorted(intervals, key=lambda pair:pair[0])             
    
    for interval in sorted_interval:
        if res and interval[0]<=res[-1][1]:
            return False
        else:
            res.append(interval)
    return True
   
    # Your solution goes here
    
    # Placeholder for the result
    # return True

# Test Cases
intervals_1 = [[0, 30],[5, 10],[15, 20]]  # Expected Output: 2
intervals_2 = [[7, 10], [2, 4]]              # Expected Output: 1
intervals_3 = [[1, 5], [2, 3], [3, 4]]      # Expected Output: 2
intervals_4 = [[1, 2], [2, 3], [3, 4]]      # Expected Output: 1

# Running the test cases
print(minMeetingRooms(intervals_1))  # Output: 2
print(minMeetingRooms(intervals_2))  # Output: 1
print(minMeetingRooms(intervals_3))  # Output: 2
print(minMeetingRooms(intervals_4))  # Output: 1
