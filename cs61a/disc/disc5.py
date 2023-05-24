def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)
        
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    '''calling branches(tree) on an empty list will return a false value,
        so not branches(tree) will be true if the list is empty'''
    return not branches(tree)

def height(t):
    # base case: we are at a single node with no branches
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(branch) for branch in branches(t)])

def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    # base case: we are at the last node in a path (leaf)
    if is_leaf(t):
        return label(t)
    
    # recursive case: add the labels of each branch until you reach a leaf,
    # this is a tree recursion and is easier to see if you draw it out on paper.
    else:
        return label(t) + max([max_path_sum(branch) for branch in branches(t)])

def find_path(t, x):
    """ input: a tree, and a value
        output: a list containing the nodes along the path from root to a node containing x
        exceptions: if no x return None
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        target = find_path(b, x)
        if target:
            return [label(t)] + target

def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    # regular solution
    '''total = 0
    for b in branches(t):
        total += sum_tree(b)
    return label(t) + total'''
    # one line solution
    return label(t) + sum([sum_tree(b) for b in branches(t)])

def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    '''I see how this works but I don't really understand the balancing
        part of it. I feel like this problem is beyond the level of what
        has been taught in the class thus far. or is just flat out confusing
        on purpose. '''
    for b in branches(t):
        if sum_tree(branches(t)[0]) != sum_tree(b) or not balanced(b):
            return False
    return True
    
    
    






    
