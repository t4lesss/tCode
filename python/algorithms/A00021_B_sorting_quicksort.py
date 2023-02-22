"""

Python > 3.10.0
github.com/t4lesss

# Algoritmo: Quick Sort.
# Algorithm: Quick Sort.

# Um algoritmo de ordenação que utiliza a estratégia de dividir para conquistar, escolhendo um elemento como pivô
# e particionando a lista a ser ordenada em duas partes, uma com elementos menores que o pivô e outra com elementos maiores.
# Esse processo é repetido recursivamente nas sub-listas resultantes até que toda a lista esteja ordenada.

# A sorting algorithm that uses the divide and conquer strategy, choosing an element as a pivot
# and partitioning the list to be sorted into two parts, one with elements smaller than the pivot and the other with elements larger.
# This process is repeated recursively in the resulting sub-lists until the whole list is sorted.

# Resumo
1    Escolhe um elemento da lista como pivô.
2    Particiona a lista em duas sub-listas, uma com elementos menores que o pivô e outra com elementos maiores.
3    Ordena as duas sub-listas recursivamente.
4    Junta as duas sub-listas ordenadas em uma só.

# Summary
1    Choose an element from the list as a pivot.
2    Partition the list into two sub-lists, one with elements smaller than the pivot and the other with elements larger.
3    Sort the two sub-lists recursively.
4    Join the two sorted sub-lists into one.


"""
import pytholino_0_1 as p;
from typing import Any;

INFO = 0; #Controla a exibição de informações adicionais. # Controls the display of additional information.

def quickSort(plist : list, ptests: bool = False) -> list[Any]:
    """
    >>> quickSort([5, 3, 8, 6, 7, 2], ptests=True)
    [2, 3, 5, 6, 7, 8]

    >>> quickSort([19, 2, 31, 45, 30, 11, 121, 27], ptests=True)
    [2, 11, 19, 27, 30, 31, 45, 121]

    >>> quickSort([1.2, 2.3, 3.4, 4.5, 5.6], ptests=True)
    [1.2, 2.3, 3.4, 4.5, 5.6]

    >>> quickSort(['d', 'b', 'a', 'c'], ptests=True)
    ['a', 'b', 'c', 'd']
    """
    n = len(plist);

    if not plist or n < 2:
        return plist

    pivot = plist[0];


    if INFO == 1 and ptests == False:
        p.p(f'Pivot:  [info]{pivot}[/info]');
    
    # Utilizo uma ab ordagem mais compacta e mais identificada com o jeito python de resolver problemas, list comprehension.
    # I use a more compact approach and more identified with the python way of solving problems, list comprehension.

    lower_list = [i for i in plist[1:] if i < pivot]
    higher_list = [j for j in plist[1:] if j >= pivot]


    if INFO == 1 and ptests == False:
        p.p(partial_list := lower_list + [pivot] + higher_list);
        p.bl();


    return quickSort(lower_list) + [pivot] + quickSort(higher_list);


@p.funkMonitor(memcheck=True, timecheck=True)
def exs():
    #ex_list = [5, 3, 8, 6, 7, 2, 9, 11, 12];
    ex_list= p.genListINT(0, 1000000, 100);
    print(quickSort(ex_list));
    p.bl();



if __name__ == '__main__':
    import doctest;
    doctest.testmod(name='bubbleSort', verbose=True);
    p.bl(2);
    
    INFO = 1;
    exs();
    



    