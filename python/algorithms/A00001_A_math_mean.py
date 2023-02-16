"""
Python > 3.10.0
github.com/t4lesss 

# Algoritmo: Média aritmética.
# Algorithm: Arithmetic mean.


    >>> mathMean([2, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 24, 26])
    12.0
    >>> mathMean([25, 74, 69, 85, 19, 22, 105, 87, 42, 24, 31])
    53.0
    >>> mathMean([1, 2, 3, 4, 5, 6, 7, 8])
    4.5


    mathMean([])
    Traceback (most recent call last):
        ...
    ValueError: List is empty


"""

import pytholino as p;

def mathMean(numbers: list) -> float: # Especifica entrada tipo lista e sapida tipo float. # Specifies input type list and sapida type float.
    if not numbers:
        raise ValueError("The list is empty");

    return sum(numbers) / len(numbers);
    #Soma dos elementos da lista dividido pelo número de elementos da lista.
    # Sum of the elements of the list divided by the number of elements of the list.


def exs():
    #p.pp(mathMean([]));
    p.pp(mathMean([25, 74, 69, 85, 19, 22, 105, 87, 42, 24, 31]));




if __name__ == "__main__":
    import doctest;
    doctest.testmod()
    exs();