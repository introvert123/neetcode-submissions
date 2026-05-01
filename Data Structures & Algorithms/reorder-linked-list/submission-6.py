# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head1: Optional[ListNode]) -> None:

        slow = head1
        fast = head1

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if not fast:# even length
            head2 = slow
            prev.next = None
        else:
            head2 = slow.next
            slow.next = None

        #reverse the second list
        prev2 = None
        curr = head2
        while curr:
            next2 = curr.next
            curr.next = prev2
            prev2 = curr
            curr = next2

        head2 = prev2

        while head1 and head2:
            next1 = head1.next
            next2 = head2.next

            head1.next = head2
            head2.next = next1

            head1 = next1
            head2 = next2
            

        