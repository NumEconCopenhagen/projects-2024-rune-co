import numpy as np

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

class IslandEconomy:
    def __init__(self, N):
        self.N = N
        self.alphas = np.random.random(N)
        self.betas = np.random.random(N)
        self.e1s = np.random.random(N)
        self.e2s = np.random.random(N)
    
    # Utility function
    def utility(x1,x2,alpha):
        return x1**alpha * x2**(1-alpha)
    
    # Production function 
    def production(z,beta):
        return z**beta
    
    # Income function
    def income(x1_pre,p1,e1,e2,beta):
        z = e1 - x1_pre
        x2_pre = e2 + production(z,beta)
        return p1*x1_pre+x2_pre
    
    # Demand functions
    def demand1(p1,alpha,I):
        return alpha*I/p1
    def demand2(alpha,I):
        return (1-alpha)*I
    
    # Excess demand functions
    def excessdemand1(e1,x1):
        return sum(e1) - sum(x1)
    def excessdemand2(e2,x2):
        return sum(e2) - sum(x2)
    


