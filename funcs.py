def n_pow_x(n, x):#replaces any numbers with n^the number unless there are 2 or more dimensions
    if type(x) == int:
        return n**x
    return [n**num for num in x]

def x_pow_n(x, n):#replaces any numbers with the number^n unless there are 2 or more dimensions
    if type(x) == int:
        return x**n
    return [num**n for num in x]

def add_lists(A, B):
    return[a + b for a,b in zip(A, B)]