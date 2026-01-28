# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(val=None, next=None)
        ptr = head
        
        while list1 or list2:
            if not list1:
                ptr.next = list2
                break
            elif not list2:
                ptr.next = list1
                break
            elif list1.val <= list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next

            ptr = ptr.next

        return head.next
