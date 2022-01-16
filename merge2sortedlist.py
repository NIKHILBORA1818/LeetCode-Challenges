'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = nik = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                nik.next = list1
                list1 = list1.next
            else:
                nik.next = list2
                list2 = list2.next
            nik = nik.next
        nik.next = list1 or list2
        return dummy.next
    
'''
Runtime: 55 ms, faster than 23.70% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.1 MB, less than 85.96% of Python3 online submissions for Merge Two Sorted Lists.
'''