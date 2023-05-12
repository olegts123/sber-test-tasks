def solution(n, k, l_lst):
  new_l_lst = l_lst.copy()
  for _ in range(k):
    current_max = max(new_l_lst)
    i = new_l_lst.index(current_max)
    new_l_lst = new_l_lst[:i] + [current_max // 2, current_max // 2
                                 ] + new_l_lst[i + 1:]
  return new_l_lst


n, k = map(int, input().split())
l_lst = []
for _ in range(n):
  new_l = int(input())
  l_lst.append(new_l)
result = solution(n, k, l_lst)
print(result)
