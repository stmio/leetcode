class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        if not head:
            return None

        ptr = head
        while ptr:
            stack.append(ptr)
            ptr = ptr.next

        revHead = stack.pop()
        ptr = revHead

        while stack:
            ptr.next = stack.pop()
            ptr = ptr.next

        ptr.next = None
        return revHead
            