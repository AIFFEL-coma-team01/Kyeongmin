class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        text = []
        num = []
        
        for i in logs:
            if i.split()[1].isdigit():
                num.append(i)
            else:
                text.append(i)
                
        # print(text)
	### 바로 밑에부분 이해 필요!!!
        text.sort(key = lambda x: (x.split()[1:], x.split()[0])) # 어떤원리지?
        # 첫번째 인자를 기준으로 오름차순 정렬 & 두번째 인자를 기준으로 오름차순 정렬
	# print(text)

        return text + num
