# endowments
e1 = 24
e2 = 0

# utility function
def u(x1,x2,alpha=1/2):
    return x1**alpha*x2**(1-alpha)

# production function
def f(z,beta=1/2):
    return z**beta