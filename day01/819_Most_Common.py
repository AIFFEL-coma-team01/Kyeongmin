import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-z]', ' ', paragraph) # 소문자 빼고 다 제외?
        '''
        for i in range(len(banned)):
            paragraph = paragraph.replace(banned[i], '')
        '''
        # 위에처럼 해버리면 abcd에서 abc를 제거한 d가 남는 상황이 생김.
        
        paragraph = paragraph.split(' ')
        paragraph = [v for v in paragraph if v not in banned and v and v != ''] ## ban list 적용, 공백제거
        print(paragraph)
        
        dic = {}
        for i in paragraph:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            
        # print(dic)
        # print(max(dic.values()))
        return max(dic, key = dic.get)
