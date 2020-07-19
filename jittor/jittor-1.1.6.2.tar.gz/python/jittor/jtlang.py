

import ast, inspect

def jiyu(func):
    return print(ast.parse(inspect.getsource(func)))

@jtlang
def func(a, b):
    c = jt.empty(a.shape, a.dtype)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i,j] = a[i,j] + b[i,j]
    return c

def __func(a, b):
    return jt.code(a.shape, a.dtype, [a, b], 
        cpu_src="""
        for (int i=0; i<a_shape0; i++)
            for (int j=0; j<a_shape1; j++)
                @c(i,j) = @a(i,j) + @b(i,j);
    """)

# 1. infer type(type assert)
# 2. infer shape(other input's shape, or const)
#       a.shape, [n], 3, [1,2,n]
# 3. infer dtype
#       a.dtype, "int"
# 4. infer output
#       jt.empty(shape, dtype)
# each statement is build or not
#  shape = a.shape not build
#  c[i,j] = a[i,j] + b[i,j]

#  for x in range(y): ---> for (int x=0; x<y; y++)

# 别名分析
# a = 1
# for ...:
#    b = a
# a = ...

# 跳转分析

# for i in range(x):
#     stmta
# for i in range(x):
#     stmtb
# stmta 和 stmtb 是否可交换

'''
每一个stmt都有自己要读的和自己要写的
'''


a = ast.parse(inspect.getsource(func))
a = a.body[0]
