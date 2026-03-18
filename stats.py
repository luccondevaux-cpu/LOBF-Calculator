def tri_diag_stats(list):
    triangle = [list]
    triangle_len_end = len(list)
    all_zeros = False
    while triangle_len_end > 1 and not all_zeros:
        all_zeros = True
        to_add = triangle[-1]
        add = []
        for i in range(len(to_add)-1):
            add_num = to_add[i+1] - to_add[i]
            add.append(add_num)
            if add_num != 0:
                all_zeros = False
        if not all_zeros:
            triangle.append(add)
            triangle_len_end = len(add)
    
    diag = []
    for i in triangle:
        diag.append(i[0])
    return triangle, diag