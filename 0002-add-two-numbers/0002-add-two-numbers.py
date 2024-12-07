# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head=ListNode()  # Create a dummmy listnode to signify list or linked list creation for the final result (will always be at start, and will point to next at end to give result)
        current=head     # create a pointer to move and create new node (created after additon) to finally create the resulting linked list
        carry=0   # Create a carry varibale to include any carry found by adding two numbers

        while l1 or l2 or carry!=0: # l1 might have 1 less node and vise varsa. Also after adding last 2 elements their might be a single value with carry. carry should be 0 to stop
            """
            Tc: O(m*n)

            2--->4--->3---->None
            5--->6--->4--->9
            """
            val1 =l1.val if l1 else 0 #(If val is pointing to None and other node is pointing to a val, update the None to 0 for adding the 2 numbers)

            val2 =l2.val if l2 else 0 
            total= val1 + val2 + carry

            current.next=ListNode(total%10)  #---> If the number after add is > 10 =, number%10 will keep the 0th position and remove 10th postion. if total<10 %10 will give the number
            
            carry = total//10 #--> If num >10 this will take val at 10th position to get the carry which will be added to next two node. if total < 10. //10 gives 0

            current=current.next # After creating the new added, update the current to point to new node
            l1= l1.next if l1 else None # Move to next node if the node exits else update to None.. same for below
            l2= l2.next if l2 else None

        return head.next
