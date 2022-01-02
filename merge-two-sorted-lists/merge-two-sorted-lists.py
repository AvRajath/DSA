# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l3 = ListNode()
        curr = l3
        while list1 != None or list2 != None:
            if list1 != None:
                if list2 != None:
                    if list1.val < list2.val:
                        curr.next = ListNode()
                        curr.next.val = list1.val
                        list1 = list1.next
                    else:
                        curr.next = ListNode()
                        curr.next.val = list2.val
                        list2 = list2.next
                else:
                    curr.next = ListNode()
                    curr.next.val = list1.val
                    list1 = list1.next
            else:
                curr.next = ListNode()
                curr.next.val = list2.val
                list2 = list2.next
            curr = curr.next
        return l3.next
        