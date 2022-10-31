import math 
def vector_distance(v1, v2, **kwargs):
    if kwargs.get("norm")=='manhattan':
        return sum([ abs(int(x)-int(y)) for x,y in zip(v1,v2) ])
    def sum_square(v):    
        return sum(list(map((lambda x: x**2), v)))
    if kwargs.get("norm")=="cosine":
        a=[int(x)*int(y) for x,y in zip(v1,v2)]
        return f'{sum(a)/math.sqrt(sum_square(v1)*sum_square(v2)):.9f}'
    else:
        return f'{math.sqrt(sum([(int(x)-int(y))**2 for x,y in zip(v1,v2)])):.1f}'
