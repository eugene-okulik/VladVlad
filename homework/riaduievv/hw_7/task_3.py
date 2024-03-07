def add_num(number):
    words = number.split()
    last_word = words[-1]
    return int(last_word) + 10


result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'
result4 = 'результат: 2'

print(add_num(result1))
print(add_num(result2))
print(add_num(result3))
print(add_num(result4))
