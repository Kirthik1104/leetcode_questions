# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res=head # Just stroring thr pointer to the head, not using anywhere in the loop. Useful for returning the head in the end.

        """ 
        1) why using head and head.next?
        --> Since we are comparing two adjacent values and comparing them, so for that we need to compare the head node and head.next node
        --> Edge using this while loop:----->if single node in list, while loop will exit for head.next because head.next is None
        --> res will return head

        2) if adjacent nodes are equal?--->head.val==head.next.val ?
        head.next = head.next.next

        head.next=head.next.next---->assign the next pointer to point to its next pointer

        [1,1,2]
          1      ==      1
        head.val == head.next.val
         1.next      1.next(1).next(2)
        head.next = head.next.next------------> pointed to third pinter



        3) If adjacent nodes are not equal?
        --> simply move the head to next pointer and then while will start compairing from the pointer whihc we moved recently with its next pointer

        4) Why store head in res?
        --> Since we are moving the head we need to somehow return the head, so we are using res to reference the head. And in the end res returns head
        -->


        Tc: 
        Time Complexity: O(n), where n is the number of nodes in the linked list.
        pace Complexity: O(1), as the algorithm is in-place.

        """

        while head and head.next: 
            if head.val==head.next.val:
                head.next=head.next.next
            else:
                head=head.next
        return res