"""
Python > 3.10.0
github.com/t4lesss 

# Em um conjunto de dados, a moda é aquele resultado mais recorrente, ou seja, com maior frequência absoluta.
# In a set of data, the mode is the most recurring result, that is, with the highest absolute frequency.


"""

import pytholino as p;
from typing import Any;


def mathMode(data_list : list) -> list[Any]: # Especifica entrada tipo lista e sapida tipo lista contendo qualquer tipo possível. # Specifies input type list and sapida type list containing any possible type.
    """

    The data_list may contain any data structure or any datatype.

    >>> mathMode([2, 3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 2, 2, 2])
    [2]
    >>> mathMode([3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 4, 2, 2, 2])
    [2]
    >>> mathMode([3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 4, 4, 2, 2, 4, 2])
    [2, 4]
    >>> mathMode(["V", "z", "y", "V", "X"])
    ['V']
    >>> mathMode(["verde", "verde" , "azul", "azul", "vermelho"])
    ['azul', 'verde']
    
    # Repare que existe ordenação pelo metodo sorted() # Note that there is sorting by the sorted() method

    """
    if not data_list:
        return [];
    count_list  = [data_list.count(value) for value in data_list];
    # Counts the number of times each value appears in data_list and creates a mirror list with the counters.
    # Conta o número de vezes que cada valor aparece em data_list e cria uma lista espelho com os contadores.
    
    y = max(count_list);  #Pega o valor do maior contador. # Gets the value of the largest counter.

    # 1. Cria uma SET com os valores que aparecem o maior número de vezes.
    # 1. Creates a SET with the values that appear the most number of times.
    # 2. SETs não podem ter valores repetidos.
    # 2. SETs cannot have repeated values.
    # 3. enumerate() retorna o índice e o valor do elemento da lista, como um dicionário.
    # 3. enumerate() returns the index and value of the list element, as a dictionary.
    # 4. Comparando, índice com índice, o if verifica se cada linha da lista espelho tem o mesmo valor do maior contador.
    # 4. Comparing, index with index, the if verifies if each row of the mirror list has the same value as the largest counter.
    # 5. Se sim, o valor é adicionado ao SET. Como não há repetições, temos a moda.
    # 5. If so, the value is added to the SET. As there are no repetitions, we have the mode.

    return sorted({data_list[i] for i, value in enumerate(count_list) if value == y});


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    p.pp(mathMode(["a", "a", "y", "y", "z", "f", "f"]));
    p.pp(mathMode(["x", "f", "f", "z", "z"]));