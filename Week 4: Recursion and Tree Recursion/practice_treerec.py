def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

def cascade2(n):
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

# Tree structure
# Counting Partitions
# Re decom: simpler instances
# 2 possibilities: 1.one 4 2.not use 4
# 2 simpler problems
# Tree recursion involves different choices
# base case
