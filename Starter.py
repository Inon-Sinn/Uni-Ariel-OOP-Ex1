def foo(f, a):
    return f(a)


def my_f(a):
    return a ** 3


c = lambda d: d ** 3
if __name__ == '__main__':
    print(foo(lambda d: d ** 3, 3))
