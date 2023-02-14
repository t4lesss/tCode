"""
Two functions are given below:


def isNested(array):
    if len(array) == 0:
        return False
    return all(isinstance(row, list) for row in array)
 
 
def isAllEQUAL(iterator):
    return len(set(iterator)) <= 1


Define a function called is_valid_array() that checks if a matrix can be built from the passed list. You can use the given functions in your solution. The passed list must be a nested list, and each nested list should consist of the same number of elements.



Example:



[IN]: is_valid_array([[3], [4]])
[OUT]: True


[IN]: is_valid_array([[3, 4], [4, 5]])
[OUT]: True


[IN]: is_valid_array([[3, 4, 5], [4, 5]])
[OUT]: False


[IN]: is_valid_array([[3, 4], [4, 5], [3, 1]])
[OUT]: True


[IN]: is_valid_array([[]])
[OUT]: True


You don't need to implement validation in your solution.



Note! You only need to define the function.


"""

# A idéia é simples. Primeiro, verificar se a lista é aninhada. Se sim, verificar se todos os elementos são iguais. Se sim, a função isValidARRAY() retorna True. Se não, retorna False.
# The idea is simple. First, check if the list is nested. If so, check if all elements are equal. If so, the function isValidARRAY() returns True. If not, returns False.

# Para a verificação, conta-se a quantidade de elementos de cada linha e coloca-se em um conjunto. Se o conjunto tiver apenas um elemento, todos os elementos são iguais.
# To verify, count the number of elements of each row and put it in a set. If the set has only one element, all elements are equal.

import pytholino as p;

# Referente ao exercício 00006_A_nestedlists.py
# Related to exercise 00006_A_nestedlists.py
def isNested(array):
    if len(array) == 0:
        return False;
    return all(isinstance(row, list) for row in array);


def isAllEQUAL(iterator):
    return len(set(iterator)) <= 1;


def isValidARRAY(array):
    if isNested(array):
        if  isAllEQUAL(len(row) for row in array):
            return True;
    return False;


#Invoke the function with the following test data:
p.p('#1. A empty list.');
p.p(isValidARRAY([]));

p.p('#2. A list with a single element.');
p.p(isValidARRAY([1]));

p.p('#3. A list with a single list.');
p.p(isValidARRAY([[]]));
p.plp();

p.p('#4. A list with a single list with a single element.');
p.p(isValidARRAY([[1]]));
p.plp();

p.p('#5. A list with a single list with two elements.');
p.p(isValidARRAY([[1, 2]]));
p.plp();

p.p('#6. A list with two lists with two elements.');
p.p(isValidARRAY([[1, 2], [3, 4]]));
p.plp();

p.p('#7. A list with two lists with assimetric elements.');
p.p(isValidARRAY([[1, 2], [3, 4, 6]]));
p.plp();

p.p('#8. A list with three lists with assimetric elements.');
p.p(isValidARRAY([[1, 2], [3, 4, 6], [3, 4, 6, 9]]));
p.plp();

p.p('#9. A list with four lists with equal elements.');
p.p(isValidARRAY([[1, 2], [3, 4], [3, 4], [5, 12]]));
p.plp();