# Pytholino Basic
# github.com/t4lesss 

import random;
from faker import Faker;
from rich import print;
from rich.pretty import pprint;

fake = Faker()
p = print;
pp = pprint;

#Imprimeir linhas
def breakLine(n=1):
    print('\n' * n, end='');

bl = breakLine;


#Imprimeir linhas com alguns parametros
def printLines(n=1, strenght=1, spaces=1, volume=20, symbol='+'):

    for i in range(n):

        print('\n' * spaces, end='');

        for i in range(strenght):
             print(*[symbol for l in range(volume)], sep='')
        
        print('\n' * spaces, end='');

plp = printLines;



############################################################################################################

def numbersRandom(min_num, max_num):
    return random.randint(min_num, max_num)

def dataStructuresFAKE(n, str_int = 0):
    data_list = []
    for i in range(n):

        datatype_list = random.choice([list, dict, set, tuple, int, str]) if str_int != 0 else random.choice([list, dict, set, tuple]);

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

############################################################################################################