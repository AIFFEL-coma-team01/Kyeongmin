def shift(li):
        temp = li[0]
        
        for i in range(1, len(li)):
            li[i-1] = li[i]
            
        li[-1] = temp
        
        return li

class Solution(object):    
    def productExceptSelf(self, nums):
        output = []
        
        for i in range(len(nums)):
            shift(nums) # [2, 3, 4, 1]
            multi = 1
            
            for i in range(len(nums) -1):
                multi *= nums[i]
            output.append(multi)
            
            
            
        return output

## Time exceeded 뜸.
## 근데 testcase가 너무한거 같다..
