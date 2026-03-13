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
    length = len(diag)
    print("length", length)
    print()


def n_pow_x(n, x):#replaces any numbers with n^the number unless there are 2 or more dimensions
    if type(x) == int:
        return n**x
    return [n**num for num in x]

def combine_lists(A, B):
    return[a + b for a,b in zip(A, B)]

#polynomial_magic([num**4 for num in range(6)])#y=x^4
polynomial_magic(combine_lists(n_pow_x(2.5, range(4)), n_pow_x(1.5, range(4))))#y=2.5^x+1.5^x