class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        holy = {}
        
        for num in nums:
            if num in holy:
                holy[num] += 1
            else:
                holy[num] = 1
                
        # print(holy)
        holy = sorted(holy.items(), key=lambda x: x[1], reverse=True)
        # print([holy[0][0], holy[1][0]])
        
        return [holy[i][0] for i in range(k)]
