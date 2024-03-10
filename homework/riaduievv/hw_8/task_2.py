import sys
sys.set_int_max_str_digits(1000000)


def gen_num():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = gen_num()
count = 0
while True:
    count += 1
    fib_num = next(fib)
    if count == 5:
        print(fib_num)
    elif count == 200:
        print(fib_num)
    elif count == 1000:
        print(fib_num)
    elif count == 100000:
        print(fib_num)
        break
