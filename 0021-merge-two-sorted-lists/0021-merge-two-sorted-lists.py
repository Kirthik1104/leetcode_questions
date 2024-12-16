# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       

        dummy=ListNode(0)
        current=dummy

        while list1 and list2:
                if list1.val<list2.val:
                    current.next=list1
                    list1=list1.next
                else:
                    current.next=list2
                    list2=list2.next
                current=current.next

        # If the 
        if list1:
            current.next=list1
        else:
            current.next=list2
            
        return dummy.next


"""
Why Two-Pointer Works Well Here
Efficiency: The two-pointer technique allows you to efficiently traverse both lists in a single pass. This means the time complexity is O(n+m), where \U0001d45b and \U0001d45a are the lengths of the two lists.

    """
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         # maintain an unchanging reference to node ahead of the return node.
#         prehead = ListNode(-1)

#         prev = prehead
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 prev.next = l1
#                 l1 = l1.next
#             else:
#                 prev.next = l2
#                 l2 = l2.next
#             prev = prev.next

#         # At least one of l1 and l2 can still have nodes at this point, so connect
#         # the non-null list to the end of the merged list.
#         prev.next = l1 or l2

#         return prehead.next