class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                for j in button[digits[i]]:
                    dfs(i+1, path+j)
            
            
        # 예외처리
        if not digits:
            return []
        
        button = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        dfs(0, "") # 0번째 index부터 탐색
        
        return result
