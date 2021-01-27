# 206. Reverse Linked List

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        
        l = []
        
        while head:
            l.append(head.val)
            head = head.next
            
        l.reverse()
        
        temp = ListNode()
        head = temp
        for i in range(len(l) -1):                
            head.val = l[i]
            if (i == len(l) -1):
                break
            head.next = ListNode()
            head = head.next
                    
        head.val = l[-1]
        
        return temp
