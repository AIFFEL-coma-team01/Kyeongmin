# 15 3Sum

class Solution(object):
    def threeSum(self, nums):
        output = []
        nums.sort()
        
        # print(nums)
        if len(nums) < 3:
            return
        
        for a in range(0, len(nums) - 2):
            for b in range(a + 1, len(nums) -1):
                for c in range(b + 1, len(nums)):
                    if nums[a] + nums[b] + nums[c] == 0 and [nums[a], nums[b], nums[c]] not in output:
                        output.append([nums[a], nums[b], nums[c]])
        
        
        return output


### Runtime Error 시간초과 ###
### for문 여러번 쓰면 안되는거 같음.. ###

