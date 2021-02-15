# 328 Odd Even Linked List

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        
        
        pointer1 = head
        pointer2 = head.next
        conn = head.next
        
        while pointer1.next and pointer2.next:
            pointer1.next = pointer1.next.next
            pointer2.next = pointer2.next.next
            
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            
        pointer1.next = conn
        
        
        return head
