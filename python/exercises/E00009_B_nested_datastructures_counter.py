"""
github.com/t4lesss 

Pegando o exercício anterior, crie uma função que retorne True se a lista apenas contiver estruturas de dados aninhadas e False se não contiver.
Depois, crie uma maneira de contar quantas estruturas de dados aninhadas existem na lista, especificando por tipo.

Taking the previous exercise, create a function that returns True if the list only contains nested data structures and False if it does not contain.
Then, create a way to count how many nested data structures exist in the list, specifying by type.


"""

import pytholino as p;

# Cria uma função que retorna um dicionário com a contagem de cada tipo de estrutura de dados aninhada.
# Creates a function that returns a dictionary with the count of each type of nested data structure.
def isNestedCounter(array):
    if len(array) == 0:
        return {};
    
    counter = {}; #Cria um dicionário vazio. #Creates an empty dictionary.
    for row in array:

        #Verifica se a linha é uma lista, dicionário, conjunto, tupla, inteiro ou string e soma 1 ao contador/chave.
        #Checks if the row is a list, dictionary, set, tuple, integer or string and adds 1 to the counter/key.
        if isinstance(row, (list, dict, set, tuple, int, str)): 
            if type(row) in counter:
                counter[type(row)] += 1;
            else:
                counter[type(row)] = 1;
    return counter; #Retorna o dicionário com a contagem de cada tipo de estrutura de dados aninhada. #Returns the dictionary with the count of each type of nested data structure.

    

def isNested(array):
    if len(array) == 0:
        return False;
    return all(isinstance(row, (list, dict, set, tuple)) for row in array);

#Para comentários, ver o arquivo 00008_A_nested_datastructures.py
#For comments, see the file 00008_A_nested_datastructures.py

arrays_list = p.dataStructuresFAKE(20,0);
p.p(isNested(arrays_list));
p.p(isNestedCounter(arrays_list));


arrays_list_02 = p.dataStructuresFAKE(20,1);
p.p(isNested(arrays_list_02));
p.p(isNestedCounter(arrays_list_02));