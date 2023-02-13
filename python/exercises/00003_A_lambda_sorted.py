"""
github.com/t4lesss 

Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


"""

p = print;

p('\n');

tuples_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]; p(f'Original: {tuples_list}'); p(f'Reordered: {sorted(tuples_list, key = lambda x: x[1])}');

# As opções de ordenação são: key = lambda x: x[0] e key = lambda x: x[1], ou seja, ordenar por ordem alfabética (nomes) ou por ordem numérica (notas).
# The sorting options are: key = lambda x: x[0] and key = lambda x: x[1], which means sorting in alphabetical order (names) or in numerical order (grades).

p('\n \n \n ');

p('Reversed: '); p(sorted(tuples_list, key = lambda x: x[1], reverse = True));

p('\n \n \n ');

p('Reversed, by name: '); p(sorted(tuples_list, key = lambda x: x[0], reverse = True));

p('\n \n \n ');

tuples_list += [('Portuguese', 100), ('History', 95), ('Geography', 87), ('Polish', 100), ('Politics', 100), ('Arts', 98), ('Python Programming', 100)]; p(f'More elements: {tuples_list}');
# Forma mais fácil de adicionar novas tuplas.
# Easier way to add new tuples.

p('\n \n \n ');

p(f'Sorted, does not modify the original list: {sorted(tuples_list, key = lambda x: x[1])}'); p('\n');
# The second criterion is the original list order.

p(f'Sorted, with a second criterion: {sorted(tuples_list, key = lambda x: (x[1], x[0]))}');
# Adding a second criterion.

p('\n \n \n ');

p(f'Original list: {tuples_list}');1
tuples_list.sort(key = lambda x: x[1]); p(f'Original list, with "sort": {tuples_list}');

p('\n');

