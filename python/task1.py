import re

def solution(input_string):
  numbers = re.findall(r'(\d{2,4}\\\d{2,5})', input_string)
  for i in range(len(numbers)):
      if len(numbers[i]) < 10:
          left, right = numbers[i].split('\\')
          left = '0' * (4 - len(left)) + left
          right = '0' * (5 - len(right)) + right
          numbers[i] = left + '\\' + right
  return numbers
  
input_string = input()
numbers = solution(input_string)
for number in numbers:
    print(number)
