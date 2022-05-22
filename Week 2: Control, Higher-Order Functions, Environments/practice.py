form operator import add
def curry2(f):
  def g(x):
    def h(y):
      return f(x,y)
    return h
  return g
add(2,3)
#currying: transforming a mul argu func into a single argu func

def print_all(x):
  print(x)
  return print_all
print_all(1)(3)(5)

def print_sum(x):
  print(x)
  def next_sum(x):
    return print_sum(x+y)
  return next_sum
#self-reference

def make_adder(n):
  def adder(k):
    return k + n
  return adder

def square(x):
  return x * x

def triple(x):
  return 3 * x

def compose1(f,g):
  def h(x):
    return f(g(x))
  return h

squiple = compose1(square,triple)
squiple(2)
compose1(square,make_adder(2))(3) #make adder 1st called
#FUnction Composition

def f(x,y):
  return g(x)
def g(a):
  return a + y
f(1,2) #error func
#local name
