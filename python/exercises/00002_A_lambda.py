"""
github.com/t4lesss 

2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75

"""

p = print;

def calc(n):
    return lambda x : x*n;

p(f'Double the number of 15 = {calc(2)(15)}.');
p(f'Triple the number of 15 = {calc(3)(15)}.');
p(f'Quadruple the number of 15 = {calc(4)(15)}.');
p(f'Quintuple the number 15 = {calc(5)(15)}.');

p('---------')

double = calc(2); p(double(10));

"""
calc(2)(15) equivale a chamar a função calc(2) e passar o argumento 15 para a função lambda. Na primeira chamada, é retornado não um valor, mas uma FUNÇÃO lambda que multiplica o argumento x por 2.
Na segunda chamada, é passado o argumento 15 para a função lambda, que retorna o resultado da multiplicação.

calc(2)(15) is equivalent to calling the function calc(2) and passing the argument 15 to the lambda function. In the first call, a value is not returned, but a lambda FUNCTION that multiplies the argument x by 2.
In the second call, the argument 15 is passed to the lambda function, which returns the result of the multiplication.

"""