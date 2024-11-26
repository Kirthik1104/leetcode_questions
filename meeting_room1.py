# Meeting Room Scheduler

## Problem Description

Given an array of meeting time intervals, each represented by a pair of start and end times `[[start_1, end_1], [start_2, end_2], ...]` (where `start_i < end_i`), determine if a person can add all meetings to their schedule without any conflicts.

### Function Signature:
```python
def can_schedule_meetings(intervals: List[Tuple[int, int]]) -> bool:



from typing import List

def minMeetingRooms(intervals: List[List[int]]) -> bool:
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
