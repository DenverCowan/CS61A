def multiply(m, n):
    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)

def skip_mul(n): # find the bug probblem. The bug was that the base case was wrong.
    if n < 2:
        return 1
    else:
        return n * skip_mul(n-2)

def is_prime(n):
        
    def prime_helper(i):
        if i == n: # i will always = 2 to begin with. this is the base case because if i == n then it made it from 2 to n withoout being divided with no remainder.
            return True
        elif n % i == 0 or n == 1:
            return False
        else:
            return prime_helper(i+1)
    return prime_helper(2)
# personally I think the problem is better solved by the following code
# it is essentially the exact same code just without having to create and call a helper function.
def prime_num(n, i=2):
    if n == i:
        return True
    elif n % i == 0 or n == 1:
        return False
    else:
        return prime_number(n, i + 1)

# the 1's below keep up with the number of steps in the hailstone function, they
# have nothing to do with actually computing n. I feel like this function is fine
# for something hiding in a library but I think a "length" variable would make it more
# clear if it is gonna be seen. but I was not able to implement it with an updating length variable
# because it resets the length value everytime hailstone is called recursively.
def hailstone(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 +1)


def merge(n1, n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10




    
