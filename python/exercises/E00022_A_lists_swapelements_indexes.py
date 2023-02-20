"""
github.com/t4lesss

# Define uma função chamada swap_elements() que recebe uma lista como argumento e substitui os primeiros e últimos elementos dessa lista.
# Define a function called swap_elements() that takes a list and two indices as arguments, and replaces the elements at the indicated indices.

Example:

>>> swapElementsIDX([4, 5, 6, 7, 1], 1, 2)
[4, 6, 5, 7, 1]


>>> swapElementsIDX(['A', 'B', 'C', 'D', 'E'], 4, 2)
['A', 'B', 'E', 'D', 'C']


>>> swapElementsIDX([2.1, 5.2, 6.2, 7.1, 2.6, 2.1], 3, 2)
[2.1, 5.2, 7.1, 6.2, 2.6, 2.1]


You don't need to implement validation in your solution.

"""

import pytholino as p;

# Valida se índices sao inteiros e se são menores que o tamanho da lista.
# Validates if indices are integers and if they are smaller than the list size.

# Como no exercício anterior, usa-se atribuição múltipla, mas agora com índices passados como parâmetros.
# As in the previous exercise, multiple assignment is used, but now with indices passed as parameters.

def swapElementsIDX(plist, index1, index2):
    if isinstance(index1, int) and isinstance(index2, int) and max(index1, index2) < len(plist):
        plist[index1], plist[index2] = plist[index2], plist[index1];
        return plist;
    else:
        return [];


def exs():

    list_01 = [-3, -1, 0, 2, 4]; p.pp(list_01);
    
    p.pp(swapElementsIDX([-3, -1, 0, 2, 4], 1, 7));


if __name__ == "__main__":
    import doctest;
    doctest.testmod()
    exs();