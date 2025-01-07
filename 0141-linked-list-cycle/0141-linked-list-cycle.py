# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:    
        """
        Using hashmap
        """
        hashmap={}
        current=head
        while current is not None:
            if current in hashmap:
                return True
            hashmap[current]=0          
            current=current.next
        return False


        """
        Using Hashset
        """
        # hashset=set()
        # current=head
        # while current is not None:
        #     if current in hashset:
        #         return True
        #     hashset.add(current)
        #     current=current.next
        # return False
     


















        # hashmap={}
        # while head is not None:
        #     if head not in hashmap:
        #       hashmap[head.val]=[ListNode(head.val)]
        #       print(hashmap)  
        #     if head.next is None:
        #         return False
        #     if head.next.val in hashmap:
        #         return True
        #     head=head.next
        # # return False

        