result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'

last_word1 = result1[result1.rindex(':') + 1:]
last_word2 = result2[result2.rindex(':') + 1:]
last_word3 = result3[result3.rindex(':') + 1:]

print(int(last_word1) + 10)
print(int(last_word2) + 10)
print(int(last_word3) + 10)
