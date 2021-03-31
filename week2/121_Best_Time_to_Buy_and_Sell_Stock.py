class Solution(object):
    def maxProfit(self, prices):
        dab = 0
        
        while prices:
            current = prices[0]
            prices.pop(0)
            
            # print(current, prices)
            try:
                if max(prices) - current > dab:
                    dab = max(prices) - current
            except:
                continue
            # print(dab)
        
        return dab


## Time LImit Exceeded : 이것도 testcase가 너무 악랄함.
