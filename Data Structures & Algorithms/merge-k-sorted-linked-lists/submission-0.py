# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None
        #we will merge the 2 lists at a time

        while len(lists) > 1:
            mergedList = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None #to satisfy both odd and even cases
                mergedList.append(self.mergeLists(l1,l2))
            lists = mergedList

        return lists[0]



    
    def mergeLists(self,list1,list2):

        if (not list1 and list2):
            return list2
        if (list1 and not list2):
            return list1

        dummy = head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        dummy.next = list1 if not list2 else list2
        return head.next