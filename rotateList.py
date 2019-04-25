# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #check if no elements:
        if not head:
            return []
            
        length, curr = 1, head
        #obtain the length
        while curr.next:
            length += 1
            curr = curr.next
            
        k %= length
        
        #make the linked list circular
        curr.next = head
        
        #point the cursor to the element prior to the k location.
        for i in range(length - k -1):
            head = head.next
            
         # Make it linear, and return the correct head
        last = head
        head = head.next
        last.next = None
        
        # print the 
        # while head.next:
        #     print(head.val)
        #     head = head.next
    
        return head
        
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
s1 = Solution()
s1.rotateRight(node1,4)
        