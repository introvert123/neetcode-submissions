# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #two pass solution
        #one way is calculating the length of the LL and traverse l-n so that we can reach at n node

        #one pass solution
        #traverse a right pointer for n and then traverse left and right till right reaches end
        #left would be at l - n from start and n from end
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
        




        





        