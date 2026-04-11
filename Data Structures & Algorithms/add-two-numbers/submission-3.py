# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = curr = ListNode()
        carry = 0
        num1 = num2 = 0
        while l1 or l2 or carry > 0:
            if l1:
                num1 = l1.val
            else:
                num1 = 0
            
            if l2:
                num2 = l2.val
            else:
                num2 = 0

            total = num1 + num2 + carry
            dummy.next = ListNode(total%10)
            carry = total//10

            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return curr.next
        
        