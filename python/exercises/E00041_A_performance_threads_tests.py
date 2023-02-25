"""
github.com/t4lesss

# Continuação do exercício E00040_A_performance_tests.py com a implementação de threads.
# Continuation of the exercise E00040_A_performance_tests.py with the implementation of threads.

"""
import math;
import pytholino_0_1 as p;
import threading;
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

    p.bl();
    p.pc(f'[bold]Interval size: [info]{interval_size}[/info] //  [info]{interval_start}[/info] - [info]{interval_end}[/info][bold]');



def main():

    t0 = time.time();
    tp0 = time.process_time();

    # Uma thread para cada núcleo. # One thread for each core.
    n_threads = multiprocessing.cpu_count();

    p.pc(f'[bold]Threads: [info]{n_threads}[/info][/bold]');

    n_start, n_end = 0, 100000000;
    n_interval = math.ceil((n_end - n_start) / n_threads);

    # Cria as threads. # Create new threads.
    threads = [threading.Thread(target=genCalcs2TESTS, args=(n_start + i*n_interval, n_start + (i+1)*n_interval)) for i in range(n_threads)];

    # Inicia as threads. # Start new Threads.
    for thread in threads:
        thread.start();
    

    # Espera as threads terminarem. # Wait for all threads to complete.
    for thread in threads:
        thread.join(); 
    

    t1 = time.time();
    tp1 = time.process_time();

    p.bl();

    p.pc(f'[bold]Numero de cores: [info]{ n_threads }[/info][/bold]');

    p.pc(f'[bold]Tempo total: [info]{t1 - t0}[/info][/bold]');
    p.pc(f'[bold]Tempo de processamento: [info]{tp1 - tp0}[/info][/bold]');




if __name__ == '__main__':
    main();


"""

Tempo total: 57.06831407546997
Tempo de processamento: 55.9375

"""