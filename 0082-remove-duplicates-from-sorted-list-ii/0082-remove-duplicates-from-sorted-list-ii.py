# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy=ListNode(0, head)
        curr=head
        prev=dummy
        duplicate=-101
        while curr.next:
            if curr.val==curr.next.val:
                duplicate=curr.val
            if curr.val==duplicate:
                prev.next=curr.next
            else:
                prev=prev.next
            curr=curr.next
        
        if curr.val==duplicate:
            prev.next=None
        
        return dummy.next























#         if not head:
#             return None
       
#         dummy=ListNode(0, head) #Creating a dummy node with value 0 and next pointer pointing to head
#         prev=dummy
#         curr=head # pointing curr to head, whihc would be used to traverse the nodes
#         duplicate=-101 # to keep track if 
#         while curr.next: # why stop before None? because we are comparing pairs of nodes, so comparing a node with none will give attribute error
#             if curr.val==curr.next.val: # if consecutive nodes are same
#                 duplicate=curr.val    # update the duplciate with first occurence of duplciate. it will help eliminate consecutive duplciates
            
#             if curr.val==duplicate: # it will help eliminate consecutive duplciates
#                 prev.next=curr.next # skip duplicates

#             else: 
#                 prev=prev.next  # if no duplicates are found, move the prev to curr and and move the curr to next position (check below)
            
#             curr=curr.next

#         if curr.val==duplicate: # since we are stopping before none, this case will help us remove duplicate nodes at last position
#             prev.next=None
#         return dummy.next
