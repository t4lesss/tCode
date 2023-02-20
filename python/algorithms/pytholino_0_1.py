# -*- coding: utf-8 -*-

"""
github.com/t4lesss

Pytholino - V. 0.1 [ Basic Implementation ]


"""

# Systema
import sys;
import platform;
import datetime;

# Formatação de texto
import pyfiglet;
from rich import print;
from rich.console import Console;
from rich.pretty import pprint;
from rich.theme import Theme;
from rich import inspect;
from rich.style import Style

pytholino_theme = Theme(
    {
    'primary': '#c0c640',
    'secondary': '#6cd6d6',
    'success': '#9ecd43',
    "info": "#dd79c6",
    'warning': '#f3bd39',
    'danger': '#ff6e6e',
    'tlight': '#e1e1e1',
    'tdark': '#a9a9a9'
    }
)

console = Console(theme=pytholino_theme, highlighter=None);

p = print;
pp = pprint;
pc = console.print;



########## Styles ##########

def pfig(ptext='', pfont="slant", pstyle='', pwidth='200', extras=''):
    text_art = pyfiglet.figlet_format(ptext, font=pfont, width = pwidth);
    pc(f'{text_art}', style=pstyle);

########## Styles ########## #


def bl(n=1):
    print('\n' * n, end='');

breakLine = bl;



def plp(n=1, strenght=1, spaces=1, volume=20, symbol='+'): #Imprimeir linhas com alguns parâmetros.

    for i in range(n):

        print('\n' * spaces, end='');

        for i in range(strenght):
             print(*[symbol for l in range(volume)], sep='')
        
        print('\n' * spaces, end='');

printLines = plp;



def pyver(label=''):
    print(label + ':  ' + sys.version.split()[0] if label else label + sys.version.split()[0]);

pythonVersion = pyver;



def pyos(label=''):
    print(label + ':  ' + platform.system() if label else label + platform.system());

pythonOS = pyos;



def tsiso():
    return str(datetime.datetime.now().isoformat());

timestampISO = tsiso;




def exs():
    pfig('Pytholino V. 0.1', 'slant', 'primary', 200, '');
    pc('Primary: [primary]Texto exemplo.[/primary]');
    pc('Secondary: [secondary]Texto exemplo.[/secondary]');
    pc('Success: [success]Texto exemplo.[/success]');
    pc('Info: [info]Texto exemplo.[/info]');
    pc('Warning: [warning]Texto exemplo.[/warning]');
    pc('Danger: [danger]Texto exemplo.[/danger]');
    pc('Tlight: [tlight]Texto exemplo.[/tlight]');
    pc('Tdark: [tdark]Texto exemplo.[/tdark]');



if __name__ == '__main__':
    exs();