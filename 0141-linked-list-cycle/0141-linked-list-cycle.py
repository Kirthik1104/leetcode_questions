# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:    
        """
        Using hashmap
        Tc: Thus, the overall time complexity is O(n), where n is the number of nodes in the linked list.
        Sc: The space required for the hash map is proportional to the number of nodes in the linked list, resulting in a space complexity of O(n).
       
        """
        # hashmap={}
       
        # while head is not None:
        #     if head in hashmap:  # Step 3: tail's next pointer is in hashmap (cycle detected)---> Return True
        #         return True
        #     hashmap[head]=0  # Step 1: From start node 1 to tail create a hashmap with value 0 (Note: Duplicate nodes while travelling from start to end is also unique)
        #     head=head.next   # Step 2: Traverse till tail node
        # return False # Step 4: If the tail's node next pointer does not contain any cycle and its pointing to none---> Return False


        """
        Using Fast and slow pointer
        -------------------------
        slow pointer: move pointer by 1 position
        fast pointer: move pointer by 2 position

        Tc: O(n)
        Sp: O(1)
        """

        fast_pointer=head
        slow_pointer=head
        
        while fast_pointer and fast_pointer.next:
            slow_pointer=slow_pointer.next
            fast_pointer=fast_pointer.next.next
            if slow_pointer==fast_pointer:
                return True
        return False



















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

        