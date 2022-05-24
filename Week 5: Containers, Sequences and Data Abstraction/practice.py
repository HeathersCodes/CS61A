#OH:
#https://www.youtube.com/watch?v=E-ExucW9O8E&list=PL6BsET-8jgYXdNFKK-pjgczjByDXguBiA&index=8
odds = [43, 47, 49]
len(odds)
odds[2]
odds[odds[1]-odds[2]]

num = {'I': 1, 'V': 5, 'X': 10} #sequence
num.values() #
list(num) #keys
list(num.values())
sum(num.values())
len(num)
{'I': 1, 'I': 5, 10.0: [1,2], 4: [1,2]}
#collection of key-value pair
#A key of dic cannot be a list or dic (or any mutable type) #tied to imprementation
#2 keys cannot not be equal; can be at most one val for a given key
{x: y for x, y in [[1,2],[2,3]]}

def index(keys, values, match):
    return {k: [v for v in values if match(k,v)] for k in keys}

# Containers
digits = [1, 8, 2, 8]
1 in digits
'1' in digits
[1, 8] in digits
[1, 2] in [[1, 2], 3]
getitem(digits, 2)

# for loop, yield iterable value, unpacking; for _ in range(3)
def count_same(pairs):
    """Return how many pairs have the same element repeated.

    >>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
    >>> count_same(pairs)
    2
    """
    same_count = 0
    for x, y in pairs:
        if x == y:
            same_count = same_count + 1
    return same_count
list(range(0))
#list Comprehension
odds = [1, 3, 5, 7, 9]
[x+1 for x in odds]
[x for x in odds if 25 % x == 0]
[(x if 25 % x == 0 else 1) for x in odds]

# string
's\ns'
# in and not in operators match substrings

#slicing
# process cantainer values
# some built-in func take iterable argument and aggregate them into a value
sum([2,3],4)
sum([[2,3],[5],[]])
max(range(3), key=lambda x: (x-1)**2)
all([1,2])

#what is the thing i wanna do
#base case: 2 possible
#one element or blank
#keep simplfy the problem untill u get to the base case


