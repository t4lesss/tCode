"""
github.com/t4lesss 

Define a function called is_nested() that checks if the passed list is nested and consists of elements of type list (a list of lists).
The function should return True if the list is nested and False otherwise.

"""

import pytholino as p

#Define a function called is_nested() that checks if the passed list is nested and consists of elements of type list (a list of lists).
#The function should return True if the list is nested and False otherwise.

def is_nested(array):
    if len(array) == 0:
        return False
    return all(isinstance(row, list) for row in array)

#LEN retorna o tamanho da lista. Se o tamanho for zero, a lista é vazia e a função retorna False.
#LEN returns the size of the list. If the size is zero, the list is empty and the function returns False.

#ALL verifica se todos os elementos retornados da iteração são considerados verdadeiros. Se sim, retorna True. Se não, retorna False.
#ALL checks if all elements returned from the iteration are considered true. If so, returns True. If not, returns False.

#ISINSTANCE verifica se o objeto é uma instância de uma classe ou de uma subclasse de uma classe, no caso, LIST. Se sim, retorna True. Se não, retorna False.
# Ou seja, para cada linha do array, verifica se a linha é uma lista.
#ISINSTANCE checks if the object is an instance of a class or a subclass of a class, in this case, LIST. If so, returns True. If not, returns False.
# In other words, for each row of the array, checks if the row is a list.

#Invoke the function with the following test data:
p.p('#1. Teste com uma lista vazia.')
p.p(is_nested([]));
p.plp();

p.p('#2. A list with a single element.')
p.p(is_nested([1]));
p.plp();

p.p('#3. A list with a single list.')
p.p(is_nested([[1]]));
p.plp();

p.p('#4. A list with multiple lists.');
p.p(is_nested([[1], [2], [3]]));
p.plp();

p.p('#5. A list with multiple lists and other elements');
p.p(is_nested([[1], [2], [3], 4]));
p.plp();

p.p('#6. A list with multiple lists and other elements, including strings');
p.pt(is_nested([[1], [2], [3], '4']));
p.plp();

p.p('#8. A list with multiple lists and other elements, including strings, integers and floats');
p.p(is_nested([[1], [2], [3], '4', 5, 6.0]));
p.plp();

p.p('# 9. A list with multiple lists and other elements, including strings, integers, floats and booleans');
p.p(is_nested([[1], [2], [3], '4', 5, 6.0, True, False]));
p.plp();

p.p('# 10. A list with multiple lists and other elements, including strings, integers, floats, booleans and None');
p.p(is_nested([[1], [2], [3], '4', 5, 6.0, True, False, None]));
p.plp();