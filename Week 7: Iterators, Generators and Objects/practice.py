def list_partitions(n, m):
    """List partitions.

    >>> for p in list_partitions(6, 4): print(p)
    [2, 4]
    [1, 1, 4]
    [3, 3]
    [1, 2, 3]
    [1, 1, 1, 3]
    [2, 2, 2]
    [1, 1, 2, 2]
    [1, 1, 1, 1, 2]
    [1, 1, 1, 1, 1, 1]
    """
    if n <= 0:
        return []
    elif m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in list_partitions(n-m, m)]
        without_m = list_partitions(n, m-1)
        return exact_match + with_m + without_m
def partitions(n, m):
    """List partitions.

    >>> for p in partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n <= 0:
        return []
    elif m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match.append(str(m))
        with_m = [p + ' + ' + str(m) for p in partitions(n-m, m)]
        without_m = partitions(n, m-1)
        return exact_match + with_m + without_m

def yield_partitions(n, m):
    """List partitions.

    >>> for p in yield_partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n <= 0:
        return
    elif m == 0:
        return
    else:
        if n == m:
            yield str(m)
        for p in yield_partitions(n-m, m):
            yield p + ' + ' + str(m)
        yield from yield_partitions(n, m-1)

def built_in_demo():
    """Using built-in sequence functions that return iterators 

    >>> bcd = ['b', 'c', 'd']
    >>> [x.upper() for x in bcd]
    ['B', 'C', 'D']
    >>> caps = map(lambda x: x.upper(), bcd)
    >>> next(caps)
    'B'
    >>> next(caps)
    'C'
    >>> s = range(3, 7)
    >>> doubled = map(double, s)
    >>> next(doubled)
    *** 3 => 6 ***
    6
    >>> next(doubled)
    *** 4 => 8 ***
    8
    >>> list(doubled)
    *** 5 => 10 ***
    *** 6 => 12 ***
    [10, 12]
    
    >>> f = lambda x: x < 10
    >>> a = filter(f, map(double, reversed(s)))
    >>> list(a)
    *** 6 => 12 ***
    *** 5 => 10 ***
    *** 4 => 8 ***
    *** 3 => 6 ***
    [8, 6]
    
    >>> t = [1, 2, 3, 2, 1]
    >>> reversed(t) == t #obj list_reverseiterator
    False
    >>> list(reversed(t)) == t
    True
    >>> iter(t.items())
    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> items = zip(d.keys(), d.values()) # Call next(items)
    """
    pass

def countdown(k):
    """Count down to zero.
    >>> list(countdown(5))
    [5, 4, 3, 2, 1]
    """
    if k > 0:
        yield k
        yield from countdown(k-1)

def prefixes(s):
    """Yield all prefixes of s.

    >>> list(prefixes('both'))
    ['b', 'bo', 'bot', 'both']
    """
    if s:
        yield from prefixes(s[:-1])
        yield s

def substrings(s):
    """Yield all substrings of s.

    >>> list(substrings('tops'))
    ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
    """
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
    def f(x):
    yield x
    yield x + 1
    return
    yield x + 3

def g(x):
    yield x
    yield x + 1
    return x + 2
    yield x + 3

def h(x):
    # The behavior below is not something you need to know/understand...
    y = yield from g(x)
    yield y
