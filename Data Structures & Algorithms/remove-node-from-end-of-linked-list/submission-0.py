# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        k = length - n
        prev = dummy = head

        if k == 0:
            head = head.next
            return head

        while k > 0:
            prev = dummy
            dummy = dummy.next
            k -= 1
        
        prev.next = dummy.next

        return head
        