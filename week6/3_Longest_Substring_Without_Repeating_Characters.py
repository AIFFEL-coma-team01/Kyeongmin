 # 3 Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        new = []
        result = {}
        
        if len(s) == 0: # ''인 경우
            return 0        
        elif len(s.strip()) == 0: # '  ', '   '인 경우
            return 1
        elif len(s) == 1: # 한글자인 경우
            return 1
        
        while len(s) > 1:
            for i in s:
                if i not in new:
                    new.append(i)
                elif i in new:
                    break
            
            word = ''.join(new)
            result[word] = len(word)
            new = []
            s = s[1:]
            
          
        return max(result.values())

# 발표! 책 풀이

def lengthOfLongestSubstring(self, s: str) -> int:
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        # 이미 등장했던 문자라면 'start' 위치 갱신
        if char in used and start <= used[char]:
	    start = used[char] + 1
	else: # 최대 부분 문자열 길이 갱신
	    max_length = max(max_length, index - start + 1)

	# 현재 문자의 위치 삽입
	used[char] = index

    return max_length
