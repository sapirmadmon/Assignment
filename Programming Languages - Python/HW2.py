# Sapir Madmon.   id: 209010230
# Roman Prasolov. id: 313091746

from math import sqrt


# ****************************************************
# ex1
def sum_list(lst):
    total_value = 0
    if len(lst) == 0:
        return total_value
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            total_value += lst[i][j]
    return total_value


# ****************************************************
# ex2A - generator function

def hailstone(n):
    while n != 1:
        if n % 2 == 0:
            yield int(n)
            n = n / 2
        else:
            yield int(n)
            n = n * 3 + 1
    yield int(n)


def q2_A():
    for i in hailstone(5):
        print(i)


# ex2B - via class
class hailstone_class:
    def __init__(self, value):
        self._value = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._value == 1:
            return
        if self._value % 2 == 0:
            self._value = int(self._value / 2)
        else:
            self._value = int(self._value * 3 + 1)
        return self._value


# implement while using 'hailstone_class' class
def q2_B():
    val = hailstone_class(5)
    itr = iter(val)
    print(val._value)
    current_item = next(itr, None)
    while current_item != None:
        print(current_item)
        current_item = next(itr, None)


# ex2C - via generator expression
def q2_C():
    generator = (i for i in hailstone(5))
    for num in generator:
        print(num)


# ****************************************************
# ex3

def reachable(graph, node):
    return reachable_help_method(graph, node, seen=None)


def reachable_help_method(graph, node, seen=None):
    seen = seen or []
    seen.append(node)
    current = set(node)
    adjacent = graph.get(node)

    if adjacent != None:
        current.update(adjacent)
        for sub_node in adjacent:
            if sub_node not in seen:
                current.update(reachable_help_method(graph, sub_node, seen))  # recursive

    return list(current)


# ***************************************************
# ex4
# The output represents the address of each variable in memory.
# var1 - List is mutable
# var2 - tuple is immutable
# So if we add items [4,5] to the list, it can change and its address will
# remain the same because it does not create a new instance,
# But if we add items (4,5) to a tuple that does not change,
# a new object will be created in memory with a new address for the new tuple.


# ***************************************************
# ex5A
# explain: a - is int and immutable.
# The first print shows the address of a in memory.
# But as soon as we add +2, 'a' cant be changed and therefore a new object
# is created in memory containing a = 7 with an address other than a = 2
def proof_immutable():
    a = 4
    print(id(a))
    a += 2
    print(id(a))


# ex5B
class MutableInt:

    def __init__(self, integer=0):
        self._integer = int(integer)

    def __add__(self, num):
        if isinstance(num, MutableInt):
            return MutableInt(self._integer + num._integer)
        return MutableInt(self._integer + num)

    def __iadd__(self, num):
        if isinstance(num, MutableInt):
            self._integer += num._value
        else:
            self._integer += num
        return self

    def __sub__(self, num):
        if isinstance(num, MutableInt):
            return MutableInt(self._integer - num._integer)
        return MutableInt(self._integer - num)

    def __isub__(self, num):
        if isinstance(num, MutableInt):
            self._integer -= num._integer
        else:
            self._integer -= num
        return self

    def __mul__(self, num):
        if isinstance(num, MutableInt):
            return MutableInt(self._integer * num._integer)
        return MutableInt(self._integer * num)

    def __str__(self):
        return str(self._integer)

    def __float__(self):
        return float(self._integer)

    def __int__(self):
        return int(self._integer)

    def __repr__(self):
        return 'Mutable Integer(%s)' % self._integer


def q5_b():
    mutable_int = MutableInt(5)
    print(mutable_int, end=" ")
    print(id(mutable_int))
    mutable_int += 10
    print(mutable_int, end=" ")
    print(id(mutable_int))


# ***************************************************
# ex6

def average(x, y):
    return (x + y) / 2


def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance


def sqrt(a):
    def sqrt_update(x):
        return average(a / x, x)

    def sqrt_close(x):
        return approx_eq(a / x, x)

    return improve(sqrt_update, sqrt_close)


# ***************************************************
# ex7A
def ex7A(nums):
    ls = list(filter(lambda x: x < 12, nums))
    print(sum(map(lambda y: y ** 2, ls)))


# ex7B
def ex7B(dic):
    ls = list(map(lambda x: x[1], list(dic.values())))
    return max(ls)


# ex7C
def ex7C(dic):
    max_res = ex7B(dic)
    for key, value in dic.items():
        if max_res == value[1]:
            return key


# start tests
def test_ex1():
    print("---exe 1---")
    lst = [[12, 4], [1], [2, 3]]
    print("the sum is: ", sum_list(lst))
    print()


def test_ex2():
    print("---exe 2A---")
    q2_A()
    print("---exe 2B---")
    q2_B()
    print("---exe 2C---")
    q2_C()
    print()


def test_ex3():
    print("---exe 3---")
    graph = {'a': ['b', 'c'], 'b': ['d'], 'c': [], 'd': ['a'], 'e': ['d']}
    print(reachable(graph, 'a'))
    print()


def test_ex5():
    print("---exe 5A---")
    proof_immutable()
    print("---exe 5B---")
    q5_b()
    print()


def test_ex6():
    print("---exe 6---")
    print(sqrt(256))
    print()


def test_ex7():
    print("---exe 7A---")
    nums = [60, 10, 7, 2, 1, 20]
    ex7A(nums)
    print("---exe 7B+C---")
    camera = {'LEQ2B': ('Nikon', 3.68, 4995), 'CAE5D424105': ('Cannon', 3.40, 3899)}
    print("The max resolution: ", ex7B(camera))
    print("The highest resolution camera model: ", ex7C(camera))


# unit test
if __name__ == "__main__":
    test_ex1()
    test_ex2()
    test_ex3()
    test_ex5()
    test_ex6()
    test_ex7()
