from itertools import izip, chain


class list_conprehensions():
    @staticmethod
    def exercise0():
        return sum([i ** 2 for i in range(100)])

    @staticmethod
    def exercise1(n, a):
        return [a for i in range(n)]

    @staticmethod
    def exercise2(n):
        return [(x, y, z) for x in range(1, n) for y in range(1, n) for z in range(1, n) if x ** 2 + y ** 2 == z ** 2]

    @staticmethod
    def exercise4(x, y):
        return [i for i in (izip(x, y))]

    @staticmethod
    def exercise6(xs, ys):
        return sum(x * y for (x, y) in zip(xs, ys))

    @staticmethod
    def exercise7(s='Think like a Fundamentalist Code like a Hacker', n=13):
        abc = list(map(chr, range(97, 123)))

        let2int = lambda c: abc.index(c)

        int2let = lambda n: abc[n]

        shift = lambda n, c: int2let((let2int(c) + n) % 26)

        process = lambda n, c: c if c == ' ' else shift(n, c) if c.islower() else shift(n, c.lower()).upper()

        return ''.join([process(n, x) for x in s])

    @staticmethod
    def exercise12(xs, ys):
        return list(chain(*zip(xs, ys)))

    @staticmethod
    def exercise13(n):
        return [i for i in range(1, n + 1) if n % i == 0]
