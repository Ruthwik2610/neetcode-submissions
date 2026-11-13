# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=[]
        curr=head
        while curr:
            s.append(curr.val)
            curr=curr.next
        curr=head
        while curr and curr.val == s.pop():
            curr= curr.next

        return not curr



