# 771 Jewels and Stones

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewel = list(jewels) # 문자열을 list화 하면 한글짜씩 쪼개서 들어감
        # print(jewel)
        count = 0
        
        for char in stones:
            if char in jewel:
                count += 1
                
        return count
