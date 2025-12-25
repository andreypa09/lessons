def get_odd_numbers(numbers): 
  """ 
  Возвращает список нечетных чисел из исходного списка. 
 
  Args: 
    numbers: Список целых чисел. 
 
  Returns: 
    Список нечетных чисел из исходного списка. 
  """ 
 
  odd_numbers = [] 
  for number in range(numbers): 
    if number % 2 == 1: 
      odd_numbers.append(number) 
  return odd_numbers
print(get_odd_numbers(123))