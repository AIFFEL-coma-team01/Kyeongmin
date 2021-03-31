# 1 Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums) -1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



##########################################################################
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     if (target - nums[i]) in nums:
        #         return [i, nums.index(target - nums[i])] ## 중복인 경우를 필터할 수 없음.
        
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if (target - nums[i]) == nums[j]:
                    return [i, j]
'''
