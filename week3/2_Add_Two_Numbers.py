# 2. Add Two Numbers
# 런타임도 너무 오래걸리고 무엇보다 연결리스트 방식으로 푼게 아니니까 좋지 않은 풀이라고 생각한다.

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return
        
        list1 = []
        list2 = []
        
        while l1:
            list1.append(l1.val)
            l1 = l1.next
            
        while l2:
            list2.append(l2.val)
            l2 = l2.next
            
        list1.reverse()
        list2.reverse()
        
        num1 = int(''.join(map(str, list1)))
        num2 = int(''.join(map(str, list2)))
        
        result = num1 + num2
        
        output = []
        for i in map(int, str(result)):
            output.append(i)
            
        output.reverse()
        
        temp = ListNode()
        head = temp
        for i in range(len(output) -1):                
            head.val = output[i]
            if (i == len(output) -1):
                break
            head.next = ListNode()
            head = head.next
                    
        head.val = output[-1]
        
        
        return temp


