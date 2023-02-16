"""
Python > 3.10.0
github.com/t4lesss 

# Algoritmo: Mediana
# Mediana é o valor que separa a metade maior e a metade menor de uma amostra, uma população ou uma distribuição de probabilidade.
# termos mais simples, mediana pode ser o valor do meio de um conjunto de dados.

# Algorithm: Median
# Median is the value that separates the larger half from the smaller half of a sample, a population, or a probability distribution.
# In simpler terms, median can be the value of the middle of a set of data.


"""

import pytholino as p;

def median(nums: list) -> int | float:
    """
    Find median of a list of numbers.
    Wiki: https://en.wikipedia.org/wiki/Median
    >>> median([0])
    0
    >>> median([4, 1, 3, 2])
    2.5
    >>> median([2, 1, 44, 10, 12, 7, 14, 20, 47])
    12

    Args:
        nums: List of nums

    """
    sorted_list = sorted(nums);
    length_sortedlist = len(sorted_list);
    mid_index = length_sortedlist >> 1 # Bitwise shift right operator. # Operador de deslocamento de bits para a direita.

    if length_sortedlist == 0:
        raise ValueError("List is empty");
    elif length_sortedlist == 1:
        return sorted_list[0];
    elif length_sortedlist % 2 == 0: # Even number of elements. # Número par de elementos.
        return (sorted_list[mid_index] + sorted_list[mid_index - 1]) / 2; # Average of two middle elements. # Média dos dois elementos do meio.
    else:
        return sorted_list[mid_index]; # Middle element. # Elemento do meio.




if __name__ == "__main__":
    import doctest;
    doctest.testmod();
    p.pp(median([2, 1, 44, 32, 14, 22, 1, 10, 99]));
