# utility function
def u(x1,x2,alpha):
    return x1**alpha*x2**(1-alpha)

# production function
def y(z,beta):
    return z**beta

#income
def income(x1,p1,e1,e2,beta):
    return x1*p1+e2+(e1-x1)**beta

# demand functions
def demand1(alpha,I,p1):
    return alpha*I/p1
def demand2(alpha,I):
    return (1-alpha)*I

#excess demand
def excessdemand1(e1,x1):
    return sum(e1) - sum(x1)
def excessdemand2(e2,x2):
    return sum(e2) - sum(x2)