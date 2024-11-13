import math

def P_plus(Q, V, X, P):
    return(math.ceil(V/(Q-2*X)*P)/P)

def P_moins(Q, V, X, P):
    return(math.floor(V/(Q+2*X)*P)/P)