import funcs
import stats

def magic_next_num(list):
    triangle, diag = stats.tri_diag_stats(list)
    #wouldn't append 0 cause its exponential, and also figure out how loop would change things
    '''triangle.append([0])
    for i in range(len(triangle)):
        j = len(triangle) - i - 2
        new_last = triangle[j+1][-1] + triangle[j][-1]
        triangle[j].append(new_last)
    return new_last'''

def magic(list, next = None):
    if next != None:
        list.append(next)

    triangle, diag = stats.tri_diag_stats(list)
    return diag_processing(diag, True)

def diag_processing(diag, first):
    pass