import poly_est
import funcs

_2x_x3 = funcs.add_lists(funcs.n_pow_x(2, range(10)),funcs.x_pow_n(range(10),3))

print(_2x_x3)

print(poly_est.magic(_2x_x3))