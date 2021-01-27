# 근데 연결리스트로 풀어야 하는데 자꾸 선형리스트로 풀어버리네;

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
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
            
        output = list1 + list2
        output.sort()
        
        
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
