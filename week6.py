import ctypes
import random
from functools import partial

def exercise1(pred, l):
    if not l:
        return False
    elif len(l) == 1:
        return pred(l[0])
    else:
        return pred(l[0]) and exercise1(pred, l[1:])


def exercise2(pred, l):
    if not l:
        return False
    elif len(l) == 1:
        return pred(l[0])
    else:
        return pred(l[0]) or exercise1(pred, l[1:])


def exercise3(pred, l):
    assert type(l) == list
    if not l:
        return l
    else:
        if pred(l[0]):
            return [l[0]] + exercise3(pred, l[1:])
        else:
            return []


def exercise4(pred, l):
    assert type(l) == list
    if not l:
        return l
    else:
        if pred(l[0]):
            return exercise4(pred, l[1:])
        else:
            return l


def exercise5(pred, l):
    return [pred(el) for el in l]


def exercise6(pred, l):
    if not l:
        return l
    else:
        return [el for el in l if pred(el)]


def exercise7(l):
    if not l:
        return 0
    else:
        return l[0] * 10 ** (len(l) - 1) + exercise7(l[1:])


def exercise9(f):
    def wrapped(*args):
        return partial(f, args[0])
    return wrapped

# f = exercise9(lambda x, y: x + y)
# print(f(1)(2))


def unfold(p, h, t, x):
    if p(x):
        a = []
    else:
        a = [h(x)] + unfold(p, h, t, (t(x)))
    return a


def exercise11(l, n):
    return unfold(lambda x: len(x) < 1, lambda x: x[:n], lambda x: x[n:], l)


def exercise12(f, l):
    return unfold(lambda x: x == [], lambda x: f(x[0]), lambda x: x[1:], l)


def idd(ob):
    return ctypes.cast(id(ob), ctypes.py_object).value

def exercise13(f, x):
    return unfold(lambda x: f(x) > 100, idd, f, x)

