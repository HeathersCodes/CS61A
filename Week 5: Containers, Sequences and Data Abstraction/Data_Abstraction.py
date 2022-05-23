# Constructor and selectors
# all of our manioulation of the num is written in terms of these func
# these fun implement an abtract data type for rational numbers
# we did not define the numer(x) yet, but we know tools we use to access the parts of rational num
# or create new rational num
# write func in terms of these then implement them
def add_rational(x, y):
    """The sum of rational numbers X and Y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    """The product of rational numbers X and Y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    """True iff rational numbers X and Y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

# i.e. rational num can be expressed by 2 parts. 2 integers tell us exactly what fraction we have
# if we can compose and decompose rational number
# constructor: compose selctor: decompose
from frsction import gcd
def rational(n, d):
    """A representation of the rational number N/D."""
    g = gcd(n, d)
    return [n//g, d//g]
#constructor of abstract data type for rational numbers
# do not have to change add_rational(x, y), just change rational 
# cuz everything defined in terms of the func

def numer(x):
    """Return the numerator of rational number X."""
    return x[0]

def denom(x):
    """Return the denominator of rational number X."""
    return x[1]
# treating rationals as whole data values
# maintain ab barries is so that u can change your data repr without change entried codes
# cons and selctor func work together to specify the right behavior


def rational(n, d):
    """A representation of the rational number N/D."""
    g = gcd(n, d)
    n, d = n//g, d//g
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select #constructor: high order func

def numer(x):
    """Return the numerator of rational number X in lowest terms and having
    the sign of X."""
    return x('n') #call the obj itself 

def denom(x):
    """Return the denominator of rational number X in lowest terms and positive."""
    return x('d')










