# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #naming is damn bad
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        dummy = ListNode()
        if fast == None:
            prev.next = None
            dummy.next = slow
            
        elif fast.next == None:
            dummy.next = slow.next
            slow.next = None
            

        #reverse the second list
        prev = None
        curr = dummy.next

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #merge both lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

            
        