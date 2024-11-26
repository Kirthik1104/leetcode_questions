import heapq
class Rooms:
  def minMeetingRooms(intervals: List[List[int]]) -> int:

    #Edge case 1
    if intervals is None:
      return []

    #Edge case 2
    if len(intervals)==1:
      return intervals
    
 

    # Step 1: Sort the meetings in increasing order of start time
    sorted_intervals=sorted(intervals, key=lambda pair:pair[0])  # sorted returns a new modified list instead of modifying the original list
    intervals.sort(key=lambda pair:pair[0])  # sort modifies the original list and does not returns a new list
    # anything can be used to sort the sub array based on first element

    
     # Step 2: Initialize a min-heap to keep track of the end times of meetings
    min_heap=[]

    # Step 3: Add the first meeting's end time to the heap
    heapq.heappush(min_heap, intervals[0][1]) 

     # Step 4: Process the remaining meetings
    for interval in intervals[1:]:
       # If the current meeting starts after or when the earliest ending meeting ends
      if min_heap[0]<=interval[0]:
        heapq.heapop(min_heap)  # Reuse the room (pop the earliest ending meeting)
      # Push the current meeting's end time to the heap
      heapq.heappush(min_heap, interval[1])

   # Step 5: The size of the heap is the minimum number of rooms required
  return len(min_heap)


#Examples
Example 1: [[0, 5], [2, 7], [6, 8]]
Step 1: Sort the meetings by start time
Sorted intervals: [[0, 5], [2, 7], [6, 8]] (already sorted)
Step 2: Initialize the min-heap
Push the end time of the first meeting (5) into the heap.

Min-Heap: [5] (One room is used for the first meeting, ending at 5).
Step 3: Process the second meeting [2, 7]
The start time of the current meeting is 2, and the earliest end time in the heap is 5.

Since 2 < 5, we cannot reuse the room, so we push 7 (end time of the second meeting) into the heap.

Min-Heap: [5, 7] (Two rooms are now in use: one for [0, 5], another for [2, 7]).
Step 4: Process the third meeting [6, 8]
The start time of the current meeting is 6, and the earliest end time in the heap is 5.

Since 6 >= 5, we can reuse the room. Pop 5 from the heap and push 8 (end time of the third meeting) into the heap.

Min-Heap: [7, 8] (Room 1 is reused for the third meeting [6, 8], and Room 2 remains for the second meeting [2, 7]).
Final Result:
The heap has two elements ([7, 8]), so we need 2 rooms.
------------------------------------------------------------------------------------------------------------------

Example 2: [[1, 2], [2, 3], [3, 4]]
Step 1: Sort the meetings by start time
Sorted intervals: [[1, 2], [2, 3], [3, 4]] (already sorted)
Step 2: Initialize the min-heap
Push the end time of the first meeting (2) into the heap.

Min-Heap: [2] (One room is used for the first meeting, ending at 2).
Step 3: Process the second meeting [2, 3]
The start time of the current meeting is 2, and the earliest end time in the heap is 2.

Since 2 <= 2, we can reuse the room. Pop 2 from the heap and push 3 (end time of the second meeting) into the heap.

Min-Heap: [3] (Room 1 is reused for the second meeting [2, 3]).
Step 4: Process the third meeting [3, 4]
The start time of the current meeting is 3, and the earliest end time in the heap is 3.

Since 3 <= 3, we can reuse the room. Pop 3 from the heap and push 4 (end time of the third meeting) into the heap.

Min-Heap: [4] (Room 1 is reused for the third meeting [3, 4]).
Final Result:
The heap has one element ([4]), so we need 1 room.

------------------------------------------------------------------------------------------------------------------
Example 3: [[0, 30], [5, 10], [15, 20]]
Step 1: Sort the meetings by start time
Sorted intervals: [[0, 30], [5, 10], [15, 20]] (already sorted)
Step 2: Initialize the min-heap
Push the end time of the first meeting (30) into the heap.

Min-Heap: [30] (One meeting room is used for the first meeting, ending at 30).
Step 3: Process the second meeting [5, 10]
The start time of the current meeting is 5, and the earliest end time in the heap is 30.

Since 5 < 30, we cannot reuse the room, so we push 10 (end time of the second meeting) into the heap.

Min-Heap: [10, 30] (Two rooms are now in use: one for [0, 30], another for [5, 10]).
Step 4: Process the third meeting [15, 20]
The start time of the current meeting is 15, and the earliest end time in the heap is 10.

Since 15 >= 10, we can reuse the room. Pop the 10 from the heap and push 20 (end time of the third meeting) into the heap.

Min-Heap: [20, 30] (Room 1 is reused for the third meeting [15, 20], and Room 2 remains for the first meeting [0, 30]).
Final Result:
The heap has two elements ([20, 30]), so we need 2 rooms.
  
