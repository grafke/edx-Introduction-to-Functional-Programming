class recursive_functions():
    @staticmethod
    def exercise0(m, n):
        if n == 1:
            return m
        else:
            return m * recursive_functions.exercise0(m, n - 1)

    @staticmethod
    def exercise4(l):
        if not l:
            return True
        else:
            return l[0] and recursive_functions.exercise4(l[1:])

    @staticmethod
    def exercise5(l):
        if not l:
            return l
        else:
            return l[0] + recursive_functions.exercise5(l[1:])

    @staticmethod
    def exercise6(n, e):
        if n == 0:
            return []
        else:
            return [e] + recursive_functions.exercise6(n - 1, e)

    @staticmethod
    def exercise7(n, l):
        if n == 0:
            return l[0]
        else:
            return recursive_functions.exercise7(n - 1, l[1:])

    @staticmethod
    def exercise8(e, l):
        if not l:
            return False
        else:
            return e == l[0] or recursive_functions.exercise8(e, l[1:])

    @staticmethod
    def exercise9(xs, ys):
        if not xs or not ys:
            return xs or ys
        else:
            if xs[0] <= ys[0]:
                return [xs[0]] + recursive_functions.exercise9(xs[1:], ys)
            else:
                return [ys[0]] + recursive_functions.exercise9(xs, ys[1:])

    @staticmethod
    def exercise10(l):
        if len(l) <= 1:
            return l
        else:
            n = len(l) / 2
            return recursive_functions.exercise9(recursive_functions.exercise10(l[:n]),
                                                 recursive_functions.exercise10(l[n:]))
