result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'

word1 = result1.split()
last_word1 = word1[-1]

word2 = result2.split()
last_word2 = word2[-1]

word3 = result3.split()
last_word3 = word3[-1]

print(int(last_word1) + 10)
print(int(last_word2) + 10)
print(int(last_word3) + 10)
