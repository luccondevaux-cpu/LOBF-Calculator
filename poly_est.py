import funcs
import stats

def magic_next_num(list):
    triangle, diag = stats.tri_diag_stats(list)
    triangle.append([0])
    for i in range(len(triangle)):
        j = len(triangle) - i - 2
        new_last = triangle[j+1][-1] + triangle[j][-1]
        triangle[j].append(new_last)
    return new_last


def magic(list, next = None):
    if next != None:
        list.append(next)

    triangle, diag = stats.tri_diag_stats(list)
    return diag_processing(diag, True)


def diag_processing(diag, first):
    length = len(diag)
    if length == 0:
        return ""

    if length == 1:
        return "+" + str(diag[0])
    
    pow_diag_end = 1
    for i in range(length-1):#length 4, pow 3, pow_diag_end = 6 is an example
        pow_diag_end *= (i + 1)
    diag_end = diag[-1]/pow_diag_end
    ignore, subt_diag = stats.tri_diag_stats(funcs.x_pow_n(range(length), length-1))
    diag = [a - (b*diag_end) for a,b in zip(diag, subt_diag)]

    looping = True
    while looping:
        removed = diag.pop(-1)
        if len(diag) == 0 and diag_end == 0:
            return ""
        elif len(diag) == 0:
            looping = False
        elif diag[-1] != 0:
            looping = False

    if first:
        return str(diag_end) + "*x^" + str(length-1) + diag_processing(diag, not first)
    first = True
    return "+" + str(diag_end) + "*x^" + str(length-1) + diag_processing(diag, not first)

# How do I want to return it such that I could possibly combine with exponential stuff?
# Just with strings that I analyze?
# What's the best way to show those strings? I like how I have it rn I guess...