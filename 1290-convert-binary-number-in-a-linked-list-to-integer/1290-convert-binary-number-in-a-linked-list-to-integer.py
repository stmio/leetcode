# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ptr = head
        val = 0

        while True:
            if ptr.val == 1:
                val += 1
            if ptr.next == None:
                break

            val = val << 1
            ptr = ptr.next
        return val