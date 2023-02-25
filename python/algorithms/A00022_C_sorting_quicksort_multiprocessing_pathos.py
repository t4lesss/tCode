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
from pathos.multiprocessing import ProcessingPool as Pool
import pytholino_0_1 as p;
from typing import Any;



INFO = 0; #Controla a exibição de informações adicionais. # Controls the display of additional information.

def quickSortP(plist : list, ptests: bool = False, pdebug=False) -> list[Any]:
    """
    >>> quickSortP([5, 3, 8, 6, 7, 2], ptests=True)
    [2, 3, 5, 6, 7, 8]

    >>> quickSortP([19, 2, 31, 45, 30, 11, 121, 27], ptests=True)
    [2, 11, 19, 27, 30, 31, 45, 121]

    >>> quickSortP([1.2, 2.3, 3.4, 4.5, 5.6], ptests=True)
    [1.2, 2.3, 3.4, 4.5, 5.6]

    >>> quickSortP(['d', 'b', 'a', 'c'], ptests=True)
    ['a', 'b', 'c', 'd']
    """
    n = len(plist);

    if not plist or n < 2:
        return plist

    pivot = plist[0];

    if INFO == 1 and ptests == False and pdebug == True:
        p.p(f'Pivot:  [info]{pivot}[/info]'); 
  
    # Um teste de implementação através de paralelismo, recursão e funções lambda com lists comprehensions utilizando o módulo pathos.multiprocessing.
    # An implementation test through parallelism, recursion and lambda functions with lists comprehensions using the pathos.multiprocessing module.

    # O resultado é um desastre, o tempo de execução é inumeras vezes maior que o do algoritmo sequencial.
    # The result is a disaster, the execution time is many times greater than that of the sequential algorithm.

    # Não façam isso em casa, crianças.
    # Don't do this at home, kids.

    with Pool() as pool:
        lower_list = pool.map(lambda i: i, [i for i in plist[1:] if i < pivot])
        higher_list = pool.map(lambda j: j, [j for j in plist[1:] if j >= pivot])

        if INFO == 1 and ptests == False and pdebug == True:
            p.p(partial_list := lower_list + [pivot] + higher_list);
            p.bl();

    return quickSortP(lower_list) + [pivot] + quickSortP(higher_list)



@p.funkMonitor(memcheck=True, timecheck=True)
def exs():
    #ex_list = [5, 3, 8, 6, 7, 2, 9, 11, 12];
    ex_list= p.genListINT(0, 1000000, 10000);
    p.p(quickSortP(ex_list));
    p.bl();



if __name__ == '__main__':

    import doctest;
    doctest.testmod(name='quickSortP', verbose=True);
    p.bl(2);

    INFO = 1;
    exs();
    

"""
A função exs levou 136.590569 segundos para executar.

"""

    