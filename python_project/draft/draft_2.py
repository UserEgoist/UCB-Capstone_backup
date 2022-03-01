#!/usr/bin/python3
from sympy import bspline_basis
from sympy.abc import x
d = 3
knots = tuple([0.        , 0.        , 0.        , 0.        , 0.02294351,
       0.04879972, 0.05518663, 0.07742836, 0.09390358, 0.10765627,
       0.14230747, 0.17262726, 0.17882134, 0.18440938, 0.1918601 ,
       0.41914513, 0.42669116, 0.44021404, 0.46434795, 0.62609665,
       0.63640559, 0.64560538, 0.65161021, 0.66877457, 0.72087321,
       0.76941701, 0.77749318, 0.80396191, 0.84521244, 0.85473657,
       0.85791128, 0.85945409, 0.86817578, 0.93909621, 0.95580301,
       0.96137194, 0.96620045, 0.97102895, 1.        , 1.        ,
       1.        , 1.        ])
print(bspline_basis(d, knots, 3, x))

print(bspline_basis(3, tuple(range(5)), 0, x))