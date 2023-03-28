# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create a dummy node to hold the head of the merged list
        dummy = ListNode()
        # create a pointer to the dummy node
        curr = dummy
        
        # traverse the two lists and compare their nodes
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        # append the remaining nodes of the non-empty list to the merged list
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        
        # return the head of the merged list
        return dummy.next
