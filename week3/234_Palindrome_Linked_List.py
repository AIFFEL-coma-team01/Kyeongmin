class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 대칭 여부 판단하기!
        li = []
        
        while head:
            li.append(head.val)
            head = head.next
            
        while li:
            try:
                if li[0] == li[-1]:
                    li.pop()
                    li.pop(0)
                else:
                    return False
            except:
                break
                
        return True

'''
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # print(head)
        rev = None
        
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        
        return not rev
'''
