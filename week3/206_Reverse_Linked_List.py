# 206. Reverse Linked List
# 배열 생성 후 풀기
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

# 연결리스트로 풀기
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        answer = head
        
        if head == None:
            return
        
        while head.next:
            temp = head.next
            
            head.next = head.next.next
            temp.next = answer
            answer = temp
            
            
            # print(answer)
            
        return answer
