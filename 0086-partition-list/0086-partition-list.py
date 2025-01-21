# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:


        left=ListNode(0)
        right=ListNode(0)

        ltail=left
        rtail=right

        while head:
            if head.val<x:
                ltail.next=head
                ltail=ltail.next
            else:
                rtail.next=head
                rtail=rtail.next
            head=head.next
        
        ltail.next=right.next
        rtail.next=None

        return left.next






















#         left=ListNode(0)    # Creating a dummy node for left partition
#         right=ListNode(0)   # Creating a dummy node for right partition

#         ltail=left       # Ltail will be used to traverse left from start to end
#         rtail=right      # Rtail will be used to traverse right partiton from satrt to end

#         """
#         Order has to be preserved
#         -------------------------

#         Tc: O(n):--- Single pass
#         1) The idea is to start from the head node and compare every nodes value with x
#         2) If head's value is less than x, add it to ltail and increment the ltail
#         3) If the head's value is greater than x, add it to rtial and incremnet the rtail

#         increment head all the time

#         4) After doing this you have to connect the partition.
#         5) Connect the ltail's last node with right.next (dummy start node of rtail)
#         6) Update the rtail last node to none, to complete the chain
#         """
#         while head:
#             if head.val<x:
#                 ltail.next=head
#                 ltail=ltail.next
#             else:
#                 rtail.next=head
#                 rtail=rtail.next
#             head=head.next
        
#         ltail.next=right.next
#         rtail.next=None

#         return left.next
        