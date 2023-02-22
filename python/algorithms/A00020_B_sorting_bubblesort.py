"""

Python > 3.10.0
github.com/t4lesss

# O Bubble Sort é um algoritmo de ordenação simples que percorre a lista diversas vezes, comparando elementos adjacentes e trocando-os se
# estiverem na ordem errada. A cada passagem pela lista, o maior elemento "flutua" para o topo, daí o nome "Bubble". De fácil implementação,
# porém, sua complexidade é quadrática [O(n²)], o que significa que tende a ser muito ineficiente em listas grandes. 

# The Bubble Sort is a simple sorting algorithm that traverses the list several times, comparing adjacent elements and swapping them if
# they are in the wrong order. At each pass through the list, the largest element "floats" to the top, hence the name "Bubble". Easy to implement,
# however, its complexity is quadratic [O(n²)], which means that it tends to be very inefficient in large lists.

# Resumo

1    Percorre a lista do início ao fim.
2    Compara o elemento atual com o próximo elemento.
3    Se o elemento atual for maior que o próximo, troca as posições.
4    Continua percorrendo a lista até que nenhum elemento precise ser trocado.

# Summary

1    Traverse the list from start to finish.
2    Compare the current element with the next element.
3    If the current element is greater than the next, swap positions.
4    Continue traversing the list until no element needs to be swapped.


"""

import pytholino_0_1 as p;
from typing import Any;


INFO = 0; #Controla a exibição de informações adicionais. # Controls the display of additional information.

@p.funkMonitor(memcheck=True, timecheck=True)
def bubbleSort(plist : list, ptests: bool = False) -> list[Any]:
    """
    >>> bubbleSort([5, 3, 8, 6, 7, 2], ptests=True)
    [2, 3, 5, 6, 7, 8]

    >>> bubbleSort([19, 2, 31, 45, 30, 11, 121, 27], ptests=True)
    [2, 11, 19, 27, 30, 31, 45, 121]

    >>> bubbleSort([1.2, 2.3, 3.4, 4.5, 5.6], ptests=True)
    [1.2, 2.3, 3.4, 4.5, 5.6]

    >>> bubbleSort(['d', 'b', 'a', 'c'], ptests=True)
    ['a', 'b', 'c', 'd']
    """
    n = len(plist)
    counter_ops = 0;
    
    if INFO == 1 and ptests == False:
        p.bl();
        p.pc(f'[bold]Bubble Sort[/bold]')
        p.pc(f'[bold]Initial: [info]{plist}[/info][/bold]')
        p.bl();

    for i in range(n): #Ciclo. # Cycle.
        crtl_changes = False

        # Uso -1 para nunca acessar o último elemento.
        # Use -1 to never access the last element.
        for j in range(n - i - 1): #Parcial. # Partial.
            counter_ops += 1;
            
            # Troca se o elemento atual for maior que o próximo com o uso de atribuições múltiplas.
            # Swap if the current element is greater than the next with the use of multiple assignments.
            if plist[j] > plist[j + 1]:
                plist[j], plist[j + 1] = plist[j + 1], plist[j]
                crtl_changes = True


                if INFO == 1 and ptests == False:
                    info_l1 = f'[bold]After: [secondary]{plist[j]}[/secondary], [secondary]{plist[j+1]}[/secondary][/bold]'
                    info_l2 = f'[bold]Before: [danger]{plist[j+1]}[/danger], [danger]{plist[j]}[/danger][/bold]'
                    p.pc(f'{info_l1} // {info_l2}')

                    p.pc(f'Partial [bold]#{counter_ops}[/bold]: [tdark]{plist}[/tdark]')
                

        if not crtl_changes:
            # A plist está ordenada
            break

        if INFO == 1 and ptests == False:
            p.bl();
            p.pc(f'[bold]Cycle #{i+1}: [info]{plist}[/info][bold]')
            p.bl(2);

    return plist



def exs():
    #ex_list= [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    ex_list= p.genListINT(0, 1000000, 100);
    exsorted_list = bubbleSort(ex_list)
    p.bl();
    p.pc(f'[bold]Final: [success]{exsorted_list}[/success][/bold]')



if __name__ == "__main__":
    INFO = 1;
    exs();
    
    import doctest;
    doctest.testmod(name='bubbleSort', verbose=True);
