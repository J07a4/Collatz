import numpy as np
def Rainbow_Gradient():
    Gradient=[]
    for R, G, B in zip(
        (list(reversed(range(256))) + [0] * 256),
        (list(range(256)) + list(reversed(range(256)))),
        ([0] * 256 + list(range(256)))):
        Gradient.append(tuple(np.divide([R, G, B],255)))
    return(Gradient)
