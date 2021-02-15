# 24
# 풀이1) 선형리스트로 변환한 뒤 풀이 -> 다시 연결리스트로 변환하여 return

class Solution(object):
    def swapPairs(self, head):
        if head == None:
            return
        if head.next == None:
            return head
        
        l = []            
        while head:
            # print(head.val)
            l.append(head.val)
            head = head.next
          
        for i in range(0, len(l), 2):
            try:
                l[i], l[i+1] = l[i+1], l[i]
            except:
                continue
        
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


# 풀이2) 연결리스트로 풀이
# 책의 1번풀이
class Solution(object):
    def swapPairs(self, head):
        cur = head
        
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
            
        return head



# 풀이3) 내가 발표해야 할 풀이
# 책의 2번풀이 (책 참조!!)

######################################################################
# 직접 연결리스트 개념을 활용해서 푼 풀이

class Solution(object):
    def swapPairs(self, head):
        if head == None:
            return
        if head.next == None:
            return head
        
        temp = head.next
        head.next = head.next.next
        temp.next = head
        
        answer = temp
        
        # print(answer)
        while head.next and head.next.next:
            temp = head.next
            head.next = head.next.next
            temp.next = head.next.next
            head.next.next = temp
            
            
            head = head.next.next
            

        # print(head)
        # print(temp)
        
        # print(answer)
        return answer


