# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        if head.next == None:
            return curr
        two_step = head.next.next
        while two_step != None:
            curr = curr.next
            if two_step.next != None:
                two_step = two_step.next.next
            else:
                return curr
        return curr.next
        