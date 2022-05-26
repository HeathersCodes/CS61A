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
