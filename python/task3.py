def solution(numbers):
  return int(''.join(sorted(numbers, reverse=True)))

numbers = input().split(' ')  # ввод чисел через пробел
result = solution(numbers)
print(result)
