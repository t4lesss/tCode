"""
github.com/t4lesss

# Um exercício de performace envolvendo uma função númerica qualquer que servirá como base para testes
# com diferentes abordagens de processamento.

# A performance exercise involving any numeric function that will serve as a basis for tests
# with different processing approaches.

# A função genCalcs2TESTS() é uma função que calcula a função f(x) para um intervalo de valores de x.
# O intervalo é dividido em partes e cada parte é calculada em uma iteração do loop for.
# O número de partes é definido pelo parâmetro pparts.

# The genCalcs2TESTS() function is a function that calculates the function f(x) for a range of x values.
# The range is divided into parts and each part is calculated in an iteration of the for loop.
# The number of parts is defined by the pparts parameter.

# A função main() é a função principal que chama a função genCalcs2TESTS() e calcula o tempo total de execução.
# The main() function is the main function that calls the genCalcs2TESTS() function and calculates the total execution time.

"""

import math;
import pytholino_0_1 as p;
import time;


def genCalcs2TESTS(pstart, pend, pparts, pdebug=False):
    
    interval_start, interval_end, n_parts = pstart, pend, pparts;
    interval_size = ((interval_end - interval_start) / n_parts);
    p.bl();
    
    
    for i in range(n_parts):
        start = interval_start + i * interval_size;
        end = start + interval_size;

        p.pc(f'[bold]Part [secondary]{i}/[secondary]: [info]{start}[/info] - [info]{end}[/info][bold]');

        # calcula a função f(x) para o intervalo atual
        for x in range(int(start), int(end)):
            y = math.sin(x) + math.cos(x/2) + 2 * x ** 2 - x;
            if pdebug == True:
                p.pc(f'[tdark]x = {x}, y = {y}[/tdark]]');

    p.bl();
    p.pc(f'[bold]Interval size: [info]{interval_size}[/info][/bold]');



def main():

    t0 = time.time();
    tp0 = time.process_time();


    genCalcs2TESTS(0, 100000000, 16);
    

    t1 = time.time();
    tp1 = time.process_time();

    p.bl();

    p.pc(f'[bold]Tempo total: [info]{t1 - t0}[/info][/bold]');
    p.pc(f'[bold]Tempo de processamento: [info]{tp1 - tp0}[/info][/bold]');



if __name__ == '__main__':
    main();


"""

Tempo total: 61.52238869667053
Tempo de processamento: 42.5625

"""