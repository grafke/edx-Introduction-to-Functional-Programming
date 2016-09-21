import sys


def exercise1(s):
    if len(s) <= 1:
        sys.stdout.write(s)
    else:
        sys.stdout.write(s[0])
        exercise1(s[1:])


def exercise2(s):
    exercise1(s)
    sys.stdout.write('\n')


def exercise3():
    s = sys.stdin.read(1)
    if s == '\n':
        return ''
    else:
        return s + exercise3()


def exercise4(f):
    exercise2(f(exercise3()))


def exercise5(l):
    if not l:
        return ()
    else:
        l[0]
        return exercise5(l[1:])

