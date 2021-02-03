# 739 또 시간초과야 씨부레거

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        output = []
        
        for i in range(len(T)):
            count = 0
            point = 0
            for j in range(i+1, len(T) + 1):
                try:
                    if T[i] < T[j]:
                        count += 1
                        output.append(count - point)
                        break
                    else:
                        count += 1
                except:
                    # print(i, j)
                    output.append(0)
                    
        return output

