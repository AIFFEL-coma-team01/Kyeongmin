# 58 - 3
# 정렬 기법을 활용한 것이 아닌 내장 함수를 이용한 방법
# 연결리스트 -> 파이썬 리스트 -> 정렬 이후 다시 연결리스트로

def sortList(self, head: ListNode) -> ListNode:
  # 연결리스트를 파이썬 리스트로
  p = head
  lst: List = []
  while p:
    lst.append(p.val)
    p = p.next

  # sort를 활용한 정렬
  lst.sort()

  # 정렬된 파이썬 리스트를 다시 연결리스트로 변환
  p = head
  for i in range(len(lst)):
    p.val = lst[i]
    p = p.next

  return head
