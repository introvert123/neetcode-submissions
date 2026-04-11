# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        m = 0
        n = 0

        temp1 = l1
        num1 = 0
        while temp1:
            num1 = num1 + (temp1.val) * (10 ** m)
            temp1 = temp1.next
            m += 1

        temp2 = l2
        num2 = 0
        while temp2:
            num2 = num2 + (temp2.val) * (10 ** n)
            temp2 = temp2.next
            n += 1
        
        num = num1 + num2
        if num == 0:
            return ListNode(0)
        l3 = dummy = ListNode()
        while num > 0:
            temp = ListNode(num%10)
            dummy.next = temp
            dummy = dummy.next
            num = num//10


        return l3.next


        
        