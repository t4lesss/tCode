"""
github.com/t4lesss

# Continuação do exercício E00040_A_performance_tests.py com a implementação de multiprocessos.
# Continuation of the exercise E00040_A_performance_tests.py with the implementation of multiprocesses.

"""

import math;
import pytholino_0_1 as p;
import multiprocessing;
import time;



def genCalcs2TESTS(pstart, pend, pdebug=False):
    
    interval_start, interval_end = pstart, pend;
    interval_size = (interval_end - interval_start);
    
    # calcula a função f(x) para o intervalo atual
    for x in range(int(interval_start), int(interval_end)):
        y = math.sin(x) + math.cos(x/2) + 2 * x ** 2 - x;
        if pdebug == True:
            p.pc(f'[tdark]x = {x}, y = {y}[/tdark]]');

    p.pc(f'[bold]Interval size: [info]{interval_size}[/info] //  [info]{interval_start}[/info] - [info]{interval_end}[/info][bold]');



def main():

    t0 = time.time();
    tp0 = time.process_time();

    # Um processo para cada núcleo
    n_process = multiprocessing.cpu_count();

    p.pc(f'[bold]Processos: [info]{n_process}[/info][/bold]');

    n_start, n_end = 0, 100000000;
    n_interval = math.ceil((n_end - n_start) / n_process);

    # Cria os processos. # Create new processes.
    process_list = [multiprocessing.Process(target=genCalcs2TESTS, args=(n_start + i*n_interval, n_start + (i+1)*n_interval)) for i in range(n_process)];

    # Inicia os processos. # Start new processes.
    for process in process_list:
        process.start();

    # Espera os processos terminarem. # Wait for all processes to complete.
    for process in process_list:
        process.join();


    t1 = time.time();
    tp1 = time.process_time();
    p.bl();

    p.pc(f'[bold]Numero de cores: [info]{ n_process }[/info][/bold]');

    p.pc(f'[bold]Tempo total: [info]{t1 - t0}[/info][/bold]');
    #p.pc(f'[bold]Tempo de processamento: [info]{tp1 - tp0}[/info][/bold]');



if __name__ == '__main__':
    main();


"""

Tempo total: 20.664390087127686

"""