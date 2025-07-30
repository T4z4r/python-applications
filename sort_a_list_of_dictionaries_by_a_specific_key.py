list_of_dicts=[ {'name':'John', 'age': 30}, {'name':'Jane', 'age': 25}, {'name':'Bob', 'age': 35} ]
list_of_dicts.sort(key=lambda x: x['age'])
print("Sorted list of dictionaries by age:", list_of_dicts)