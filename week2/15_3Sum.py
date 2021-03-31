# 15 3Sum
'''
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
'''

### Runtime Error 시간초과 ###
### for문 여러번 쓰면 안되는거 같음.. ###


# Two-pointer
results = []
nums.sort()

for i in range(len(nums) - 2):
    # 중복된 값 건너뛰기
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    
    # 간격을 좁혀가며 sum 계산
    left, right = i + 1, len(nums) -1
    while left < right:
        sum = nums[i] + nums[left] + nums[right]
        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
        else:
            # sum = 0인 경우이므로 정답 및 스킵 처리 
            results.append((nums[i], nums[left], nums[right]))
            
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
                
            left += 1
            right -= 1
            
return results
