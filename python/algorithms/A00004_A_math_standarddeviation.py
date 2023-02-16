"""
Python > 3.10.0
github.com/t4lesss 

# Algoritmo: Desvio padrão.
# Algorithm: Standard deviation.

# O desvio padrão é uma medida estatística que indica o grau de dispersão dos dados em relação à média.
# Em outras palavras, é uma medida de quanto os valores individuais de um conjunto de dados diferem da média geral desse conjunto.
# Quanto maior o desvio padrão, mais dispersos são os dados em relação à média.

# The standard deviation is a statistical measure that indicates the degree of dispersion of the data relative to the mean.
# In other words, it is a measure of how far each individual value is from the average of the whole set of values.
# The higher the standard deviation, the more dispersed the data is relative to the mean.


    >>> mathStandardDEV([25, 74, 69, 85, 19, 22, 105, 87, 42, 24, 31])
    30.04

    >>> mathStandardDEV([2, 4, 6, 8, 10])
    2.83

    >>> mathStandardDEV([10, 12, 23, 23, 16, 23, 21, 16])
    4.9

    >>> mathStandardDEV([1.5, 2.7, 3.8, 4.2, 5.1])
    1.25

"""

import pytholino as p;
from A00001_A_math_mean import mathMean;

def mathStandardDEV(numbers_list: list) -> float: # Especifica entrada tipo lista e saída tipo float. # Specifies input type list and output type float.

    if not numbers_list:
        raise ValueError("The list is empty");

    mean = mathMean(numbers_list);
    # Referente ao algoritmo A00001_A_math_mean.py
    # Related to the A00001_A_math_mean.py algorithm.

    
    variance = sum((value - mean) ** 2 for value in numbers_list) / len(numbers_list);
    # Variância é uma média dos - quadrados das diferenças - entre cada valor e a média de lista enviada como argumento.
    # Variance is the average of the - squares of the differences - between each value and the mean of the list sent as an argument.


    return round((variance ** 0.5), 2);
    # Desvio padrão é a raiz quadrada da variância.
    # Standard deviation is the square root of the variance.

def exs():
    p.pp(mathStandardDEV([-3, -1, 0, 2, 4]));



if __name__ == "__main__":
    import doctest;
    doctest.testmod()
    exs();
