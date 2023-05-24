class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
         return self.x

    def __str__(self):
         return self.x * 2

class B:
    def __init__(self):
         print('boo!')
         self.a = []

    def add_a(self, a):
         self.a.append(a)

    def __repr__(self):
         print(len(self.a))
         ret = ''
         for a in self.a:
             ret += str(a)
         return ret

class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
    def __len__(self):
            return 1 + len(self.rest)

ganondorf = Link('zelda', Link('link', Link('sheik', Link.empty)))

def sum_nums(s):
    if s == Link.empty:
      return 0 # must return 0 or you will get an error about trying to add int an Nonetype
    return s.first + sum_nums(s.rest)


def multiply_lnks(lst_of_lnks):
    product = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        product *= lnk.first
    lst_of_lnks_rest = [lnk.rest for lnk in lst_of_lnks] 
    return Link(product, multiply_lnks(lst_of_lnks_rest))

    '''Description from the TA's
    For our base case, if we detect that any of the lists in the list of Links is empty,
    we can return the empty linked list as we’re not going to multiply anything.
    Otherwise, we compute the product of all the firsts in our list of Links.
    Then, the subproblem we use here is the rest of all the linked lists in our list of Links.
    Remember that the result of calling multiply_lnks will be a linked list!
    We’ll use the product we’ve built so far as the first item in the returned Link,
    and then the result of the recursive call as the rest of that Link.'''

def flip_two(s):
    if len(s) > 1:
        # Below is a python feature called parrallel assignment that allows you to avoid using
        # temporary variables to store values.
        s.first, s.rest.first = s.rest.first, s.first 
        flip_two(s.rest.rest)
    else:
        return
    
'''Came up with this solution by myself. It works as it's supposed to. but I will include the TA soln below.
    they are essentially the same as what I coded above but without the length function

    # Recursive solution:
    if s is Link.empty or s.rest is Link.empty:
        return
    s.first, s.rest.first = s.rest.first, s.first
    flip_two(s.rest.rest)

    # For an extra challenge, try writing out an iterative approach as well below!
    return # separating recursive and iterative implementations

    # Iterative approach
    while s is not Link.empty and s.rest is not Link.empty:
        s.first, s.rest.first = s.rest.first, s.first
        s = s.rest.rest
        '''
class Tree:

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

t = Tree(3, [Tree(4), Tree(5)])

def make_even(t):
    if t.label % 2 != 0:
        t.label += 1
    for b in t.branches:
        make_even(b)
'''The above solution is the one I came up with and it works. It is identical
to the TA solution. I will also include the TA's alternate solution below.
Not sure of any performance advantages either way you go.

 t.label += t.label % 2 # if even t.label %2 =0, if not = 1
    for branch in t.branches:
        make_even(branch)
return'''







    
    
    
