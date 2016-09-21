poem = ["Three Types for the Lisp-kings under the parentheses,"
    , "Seven for the Web-lords in their halls of XML,"
    , "Nine for C Developers doomed to segfault,"
    , "One for the Dark Lord on his dark throne"
    , "In the Land of Haskell where the Monads lie."
    , "One Type to rule them all, One Type to find them,"
    , "One Type to bring them all and in the Lambda >>= them"
    , "In the Land of Haskell where the Monads lie."
        ]
xs = [1, 2, 35, 2, 3, 4, 8, 2, 9, 0, 5, 2, 8, 4, 9, 1, 9, 7, 3, 9, 2, 0, 5, 2, 7, 6, 92, 8, 3, 6, 1, 9, 2, 4, 8, 7, 1,
      2, 8, 0, 4, 5, 2, 3, 6, 2, 3, 9, 8, 4, 7, 1, 4, 0, 1, 8, 4, 1, 2, 4, 56, 7, 2, 98, 3, 5, 28, 4, 0, 12, 4, 6, 8, 1,
      9, 4, 8, 62, 3, 71, 0, 3, 8, 10, 2, 4, 7, 12, 9, 0, 3, 47, 1, 0, 23, 4, 8, 1, 20, 5, 7, 29, 3, 5, 68, 23, 5, 6, 3,
      4, 98, 1, 0, 2, 3, 8, 1]

ys = map(lambda x: ((x + 1) * 3) ** 3 - 7, xs)


def triangle(N):
    if N <= 0:
        return 0
    else:
        return N + triangle(N-1)


def count(el, xs):
    if not xs:
        return 0
    else:
        if el == xs[0]:
            cnt = 1
        else:
            cnt = 0
    return cnt + count(el, xs[1:])


def euclid(a, b):
    assert a > 0 and b > 0
    if a == b:
        return a
    else:
        if a > b:
            return euclid(a - b, b)
        else:
            return euclid(b, b - a)


def funky_map(f, g, xs):
    if not xs:
        return []
    elif len(xs) == 1:
        return [f(xs[0])]
    else:
        return [f(xs[0]), g(xs[1])] + funky_map(f, g, xs[2:])


def exercise4():
    return count(101, sum(map(lambda sentence: map(lambda symbol: ord(chr(ord(symbol) + 4)), sentence), poem), []))

def exercise7():
    print(sum(funky_map(lambda x: x+10, lambda x: x+100, ys)))
    print(sum(funky_map(lambda x: 1 if x == 'e' else 0, lambda x: ord(x), ''.join(poem))))

