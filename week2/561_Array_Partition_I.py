# 561 Array Partition I

class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort(reverse = True)
        sum = 0
        totallen = len(nums)
        
        for i in range(totallen / 2):
            sum += min(nums[0], nums[1])
            
            nums.pop(0)
            nums.pop(0)
            # print(nums)
            
            
        return sum


## Runtime 너무 오래걸림.. pop을 2번써서 그런거 같음. ##
## 내 풀이 444, 책 풀이 264ms ##
