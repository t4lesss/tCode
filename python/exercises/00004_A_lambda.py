"""
github.com/t4lesss 

Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

"""

p = print;

models_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
               {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
               {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
               {'make': 'Apple', 'model': 9, 'color': 'Silver'},
               {'make': 'Apple', 'model': 16, 'color': 'Gold'},
               {'make': 'LG', 'model': 11, 'color': 'Pink'}
               ]

p(f'Original: {models_list}'); p(f'Reordered: {sorted(models_list, key = lambda x: x["color"])}');

# Ordena por cor. A chave é passada como um argumento para a função lambda.
# Sorts by color. The key is passed as an argument to the lambda function.