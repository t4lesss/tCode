"""
github.com/t4lesss 

Define a function called swap_elements() that takes a list as argument and replaces the first and last elements of that list.

Example:

[IN]: swap_elements([4, 5, 6, 7])
[OUT]: [7, 5, 6, 4]

[IN]: swap_elements([4, 5, 6, 7, 1])
[OUT]: [1, 5, 6, 7, 4]

[IN]: swap_elements([4, 5])
[OUT]: [5, 4]

You don't need to implement validation in your solution.

    >>> swapElements(['Abella Danger', 'Riley Reid', 'Mia Khalifa', 'Asa Akira', 'Emily Willis', 'Angela White'])
    ['Angela White', 'Riley Reid', 'Mia Khalifa', 'Asa Akira', 'Emily Willis', 'Abella Danger']

    >>> swapElements([4, 5, 6, 7])
    [7, 5, 6, 4]

    >>> swapElements([4, 5, 6, 7, 1])
    [1, 5, 6, 7, 4]

    >>> swapElements([4, 5])
    [5, 4]


"""

import pytholino as p;

# A idéia é exemplificar a inversão direta de elementos em uma lista através de atribuição múltipla.
# The idea is to exemplify the direct inversion of elements in a list through multiple assignment.

def swapElements(plist):
    plist[0], plist[-1] = plist[-1], plist[0]
    return plist



def exs():

    list_01 = [-3, -1, 0, 2, 4]; p.pp(list_01);
    
    p.pp(swapElements([-3, -1, 0, 2, 4]));



if __name__ == "__main__":
    import doctest;
    doctest.testmod()
    exs();