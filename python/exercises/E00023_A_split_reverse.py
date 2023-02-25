"""
github.com/t4lesss

# Defina uma função chamada reverse_words() que recebe uma sentença como argumento e inverte a ordem das palavras na sentença dada. Por questões de simplicidade, assumimos que a sentença não contém nenhum sinal de pontuação.
# Define a function called reverse_words() that takes a sentence as an argument and reverses the order of words in the given sentence. For the sake of simplicity, we assume that the sentence doesn't contain any punctuation marks.

Example:

>>> wordsReverse('python is the best')
'best the is python'


>>> wordsReverse('you should learn python language')
'language python learn should you'


You don't need to implement validation in your solution.

"""

import pytholino as p;

def wordsReverse(pstring):
    sorted_words = pstring.split()
    return ' '.join(sorted_words[::-1])
    #Slice para uma cópia reversa da lista.
    # Slice for a reverse copy of the list.



if __name__ == "__main__":
    import doctest;
    doctest.testmod(name='wordsReverse', verbose=True);
