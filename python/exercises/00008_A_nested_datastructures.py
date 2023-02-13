"""
github.com/t4lesss 

Define a function called is_nested() that checks if the passed list is nested and consists of elements of type list, dictionary, set or tuple (a list of data structures).
The function should return True if the list is nested and False otherwise.


"""

import pytholino as p;


def is_nested(array):
    if len(array) == 0:
        return False
    return all(isinstance(row, (list, dict, set, tuple)) for row in array)

#LEN retorna o tamanho da lista. Se o tamanho for zero, a lista é vazia e a função retorna False.
#LEN returns the size of the list. If the size is zero, the list is empty and the function returns False.

#ALL verifica se todos os elementos retornados da iteração são considerados verdadeiros. Se sim, retorna True. Se não, retorna False.
#ALL checks if all elements returned from the iteration are considered true. If so, returns True. If not, returns False.

#ISINSTANCE verifica se o objeto é uma instância de uma classe ou de uma subclasse de uma classe. No caso, LIST, DICT, SET ou TUPLE. Se sim, retorna True. Se não, retorna False.
# Ou seja, para cada linha do array, verifica se a linha é uma lista, dicionário, conjunto ou tupla.
#ISINSTANCE checks if the object is an instance of a class or a subclass of a class. In this case, LIST, DICT, SET or TUPLE. If so, returns True. If not, returns False.
# In other words, for each row of the array, checks if the row is a list, dictionary, set or tuple.


p.p(is_nested(p.dataStructuresFAKE(20,0)));
#Para testar a função, utilizando um gerador de estruturas de dados dentro de uma lista. A descrição da função está no arquivo 00007_B_datastructures_generator.py.
#To test the function, using a data structures generator inside a list. The description of the function is in the file 00007_B_datastructures_generator.py.

p.p(is_nested(p.dataStructuresFAKE(20,1)));