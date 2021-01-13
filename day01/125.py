import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reverse 사용하면 되지않나?
        s = re.sub('[-=+,#/\?:^$.@*_\{}"※~;&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', s) 
        s = s.replace(" ", "")
        s = s.lower()
        reverse = ''.join(reversed(s))
        # print(''.join(reversed(s)))
        # reverse = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', reverse)
        
        # print(s)
        # print(reverse)
        
        
        if s == reverse:
            return True
        else:
            return False
            
