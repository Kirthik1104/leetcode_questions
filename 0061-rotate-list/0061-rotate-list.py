# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        """
        Tc: O(n)
        """
        if not head:
            return None
        
        lastnode=head
        length=1         # Getting the length of the linked list

        while lastnode.next:  # Just stopping exactly before the None--> At last Node
            lastnode=lastnode.next
            length+=1
        
        
        k=k%length  # if k is greater than length of node's list then, this will give remainder (how many extra k is required after 1 full rotatio. (full rotation is assumed))
        # print(k)
        
        #Connect the lastnode with head---> Creating a circular linked list
        lastnode.next=head # lastnode points to 1 node before none. point lastnode.next to head----> to create a circular linked list

        tempnode=head

        """
        a=[1,2,3,4,5]
        k=2
        5-2-1=2 : To point to excalt 1 node before the rotation starts
        """
        for i in range(length-k-1): # stop one node before the rotation starts
            tempnode=tempnode.next
        
        """
        [1,2,3,4,5]
        answer= 4,5,1,2,3 --> Since its a circular linked list
        4,5,1,2,3->None  -->tempnode.next
        """
        answer=tempnode.next #
        tempnode.next=None

        return answer


        