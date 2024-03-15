def finish_me(func):
    def wrapper(value):
        func(value)
        print('finished')
    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
