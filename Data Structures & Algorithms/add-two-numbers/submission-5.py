# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = head = ListNode()
        carry = 0
        while l1 or l2:
            if l1 and l2:
                digitsSum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                digitsSum = l1.val + carry
                l1 = l1.next
            else:
                digitsSum = l2.val + carry
                l2 = l2.next


            if digitsSum >= 10:
                carry = digitsSum//10
            else:
                carry = 0

            dummy.next = ListNode(digitsSum%10)
            dummy = dummy.next
        if carry != 0:
            dummy.next = ListNode(carry)
        return head.next



        