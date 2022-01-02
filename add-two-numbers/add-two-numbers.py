# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l3 = ListNode()
        curr = l3
        while l1 != None or l2 != None:
            val1 = 0
            val2 = 0
            if l1 != None:
                val1 = l1.val
                l1 = l1.next
            if l2 != None:
                val2 = l2.val
                l2 = l2.next
            curr.next = ListNode()
            temp = curr.next
            
            temp.val = (val1+val2+carry) % 10
            if val1+val2+carry >= 10:
                
                carry = 1
            else:
                carry = 0
            curr = curr.next
        if carry == 1:
            curr.next = ListNode()
            temp = curr.next
            
            temp.val = 1
            
        return l3.next  
        