def polynomial_magic_stats(list):
    #print("input", list)
    triangle = [list]
    triangle_len_end = len(list)
    all_zeros = False
    while triangle_len_end > 1 and not all_zeros:
        all_zeros = True
        to_add = triangle[-1]
        add = []
        for i in range(len(to_add)-1):
            add_num = to_add[i+1] - to_add[i]
            #print("add_num", add_num)
            add.append(add_num)
            if add_num != 0:
                all_zeros = False
        if not all_zeros:
            triangle.append(add)
            triangle_len_end = len(add)
    
    diag = []
    for i in triangle:
        diag.append(i[0])
    print("diag", diag)
    return triangle, diag

def polynomial_magic_next_num(list):
    triangle, diag = polynomial_magic_stats(list)
    triangle.append([0])
    for i in range(len(triangle)):
        j = len(triangle) - i - 2
        new_last = triangle[j+1][-1] + triangle[j][-1]
        triangle[j].append(new_last)
    return new_last

def polynomial_magic(list, next):
    list.append(next)
    return polynomial_magic(list)

def polynomial_magic(list):
    triangle, diag = polynomial_magic_stats(list)
    return diag_processing(diag, True)


def diag_processing(diag, first):
    length = len(diag)
    print("length", length)
    if length == 0:
        return ""

    if length == 1:
        return str(diag[0])
    
    pow_diag_end = 1
    for i in range(length-1):#length 4, pow 3, pow_diag_end = 6 is an example
        pow_diag_end *= (i + 1)
    diag_end = diag[-1]/pow_diag_end
    ignore, subt_diag = polynomial_magic_stats(x_pow_n(range(length), length-1))
    diag = [a - (b*diag_end) for a,b in zip(diag, subt_diag)]
    print("diag_subt_multiple(diag_end)", diag_end)

    looping = True
    while looping:
        print("diag zero lowering", diag)
        removed = diag.pop(-1)
        print(len(diag))
        if len(diag) == 0 and diag_end == 0:
            return ""
        elif len(diag) == 0:
            looping = False
        elif diag[-1] != 0:
            looping = False
    #what to do if you remove a diag value and everything after that is 0? the return is just nothing
    #why return nothing; cause then it will get mad cause it will try to do above with nothing in diag. when diag is done, check values.

    print("updated diag", diag)

    print(first)
    if first:
        return str(diag_end) + "*x^" + str(length-1) + diag_processing(diag, not first)
    first = True
    return "+" + str(diag_end) + "*x^" + str(length-1) + diag_processing(diag, not first)


def n_pow_x(n, x):#replaces any numbers with n^the number unless there are 2 or more dimensions
    if type(x) == int:
        return n**x
    return [n**num for num in x]

def x_pow_n(x, n):#replaces any numbers with the number^n unless there are 2 or more dimensions
    if type(x) == int:
        return x**n
    return [num**n for num in x]

def combine_lists(A, B):
    return[a + b for a,b in zip(A, B)]

#Approximates the function describing the trend of a list of numbers such that the function is a polynomial of order/degree one less than the length of the list entered
print(polynomial_magic(x_pow_n(range(5), 5)))