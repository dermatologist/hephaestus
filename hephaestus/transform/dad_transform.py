import time


def transform(*args):
    time.sleep(1)
    for arg in args:
        print(arg[1])
        yield arg
