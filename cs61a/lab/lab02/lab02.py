def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    '''   using example one:
    curried_add = lambda_curry2(add) binds add to func and returns lambda x,
    add_3 = curried_add(3) binds 3 to x and returns lambda y,
    add_3(5) binds 5 to y and returns func(3,5) which is equivalent to add(3,5)
    thus turning a two parameter function into a one parameter function.'''
    return lambda x: lambda y: func(x,y)


def lambda_curry2_syntax_check():
    """Checks that definition of lambda_curry2 is one line.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(lambda_curry2)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.


def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def count_nums(n):
        i, count = 1, 0
        while i <= n:
            if condition(n , i):
                count += 1
            i += 1
        return count
    return count_nums


def composer(f, g):
    """Return the composition function which given x, computes f(g(x)). this takes in two functions as arguments.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = composer(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = composer(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))


def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    def compare(x):
        return composer(f, g)(x) == composer(g, f)(x)
    return compare



def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def num_cycles(n):
        def apply_cycles(x):
            count = 1
            while count <= n:
                if count % 3 == 1:
                    x = f1(x)
                elif count % 3 == 2:
                    x = f2(x)
                else:
                    x = f3(x)
                count += 1
            return x
        return apply_cycles
    return num_cycles
'''cylce returns a function that takes a single parameter n which represents the number of cycles to do.
that function then takes x the number on which to apply the cycles.
then when that function is called it will run n cycles on x.
the logic for applying the cycles is set the count to 1 to start which will make it automatically return x if x == 0
then we institute a while count <= n if count % 3 ==1 run f1, or count % 3 ==2 run f2, etc. this works because we have a 
cycle of 3 functions and the modulo operator (%3) will always evaluate to 1,2, or 0.
for example 101 % 3 = 2 because it always returns the whole number remainder of n divided 3
so 1 % 3 = 1 because 3 won't go into one, 2 %3 =2, 3 %3 =0, 4%3 =1, 5%3 =2, 6%3=0, etc the pattern continues forever.
then we just increment the count until x < n which breaks the loop, then we can return x and out outer functions.
'''
