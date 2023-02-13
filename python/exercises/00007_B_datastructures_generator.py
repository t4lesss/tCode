"""
github.com/t4lesss 

Data Structures Generator
Create a function that generates a list of random data structures (list, dict, set, tuple, int, str) with random data.

"""

import random;
from faker import Faker;
import pytholino as p;

fake = Faker()
# Faker é uma biblioteca que gera dados falsos para testes.
# Faker is a library that generates fake data for testing.

def numbersRandom(min_num, max_num):
    return random.randint(min_num, max_num)
# Retorna um número inteiro aleatório entre min_num e max_num.
# Returns a random integer between min_num and max_num.


def dataStructuresFAKE(n, str_int = 0):
    data_list = []
    for i in range(n):

        datatype_list = random.choice([list, dict, set, tuple, int, str]) if str_int != 0 else random.choice([list, dict, set, tuple]);
        # Escolhe um tipo de dado aleatório da lista. Se str_int for diferente de 0, os tipos de dados int e str também são adicionados.
        # Chooses a random data type from the list. If str_int is not 0, the data types int and str are also added.

        if datatype_list == list:
            data_list.append([fake.name() for j in range(numbersRandom(1, 10))])
        elif datatype_list == dict:
            data_list.append({fake.name(): fake.random_int(min=18, max=99, step=1) for j in range(numbersRandom(1, 10))})
        elif datatype_list == set:
            data_list.append({fake.city() for j in range(numbersRandom(1, 10))})
        elif datatype_list == tuple:
            data_list.append(tuple(fake.country() for j in range(numbersRandom(1, 10))))
        elif datatype_list == int:
            data_list.append(fake.random_int(min=0, max=99))
        else:
            data_list.append(fake.name())
    return data_list
# Retorna uma lista de n elementos, cada um com um tipo de dado aleatório e com dados aleatórios.
# Returns a list of n elements, each with a random data type and with random data.



fakedata_list = dataStructuresFAKE(20,0)

p.p('\n'.join([str(ds) for ds in fakedata_list]));
# Imprime a lista de dados falsos, um por linha.
# Prints the list of fake data, one per line.