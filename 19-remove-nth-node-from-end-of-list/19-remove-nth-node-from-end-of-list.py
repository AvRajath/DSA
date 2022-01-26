# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        back = head
        front = head
        n = n+1
        while n > 0:
            front = front.next
            if front == None and n!=1:
                return head.next
            n = n-1
            
        while front != None:
            front = front.next
            back = back.next
        
        temp = back.next.next
        back.next = temp
        return head
        
        
        
        