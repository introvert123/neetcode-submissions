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

        if not fast:
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

        dummy = head = ListNode()

        while head1 and head2:
            dummy.next = head1
            dummy = dummy.next
            head1 = head1.next

            dummy.next = head2
            dummy = dummy.next
            head2 = head2.next

        dummy.next = head1 if not head2 else head2
        head1 = head.next

        