# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        dummy = newHead = ListNode()
        if fast == None:
            prev.next = None
            while slow:
                dummy.next = slow
                dummy = dummy.next
                slow = slow.next
        elif fast.next == None:
            temp2 = slow.next
            slow.next = None
            while temp2:
                dummy.next = temp2
                dummy = dummy.next
                temp2 = temp2.next

        #reverse the second list
        prev = None
        curr = newHead.next

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #merge both lists
        temp = head

        while prev and temp:
            later = temp.next
            temp.next = prev
            later2 = prev.next
            prev.next = later
            temp = later
            prev = later2

            
        