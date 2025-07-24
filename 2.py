# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def addTwoNumbers(self, l1, l2):
    #     print(l1)
    #     print(l2)
    #     answer = 0
    #     mul = 1
    #     current = l1
    #     while current:
    #         answer += current.val * mul
    #         mul *= 10
    #         current = current.next
    #     mul = 1
    #     current = l2
    #     while current:
    #         answer += current.val * mul
    #         mul *= 10
    #         current = current.next
    #     linkedList = ListNode()
    #     mul = 10
    #     while answer > 0:
    #         linkedList.val = answer % mul
    #         answer = answer // mul
    #         linkedList.next = ListNode()
    #         mul *= 10
    #     return linkedList
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values (0 if node doesn't exist)
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = x + y + carry
            carry = total // 10
            
            # Create new node with ones digit
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to next nodes if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return dummy.next

print(Solution.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))