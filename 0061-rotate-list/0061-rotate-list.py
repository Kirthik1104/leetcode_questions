# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        lastnode=head
        length=1

        while lastnode.next:
            lastnode=lastnode.next
            length+=1
        
        k=k%length  # if k is greater than length of node's list then, this will give remainder (how many extra k is required after 1 full rotatio. (full rotation is assumed))
        # print(k)
        
        lastnode.next=head # lastnode points to 1 node before none. point lastnode.next to head----> to create a circular linked list

        tempnode=head

        """
        a=[1,2,3,4,5]
        k=2
        5-2-1=2 : To point to excalt 1 node before the rotation starts
        """
        for i in range(length-k-1): 
            tempnode=tempnode.next
        
        answer=tempnode.next
        tempnode.next=None

        return answer


        