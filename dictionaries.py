product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "First_name": "Fabricio",
    "Last_name": "  Gutierrez" 
}
#print(dir(product))         #Para ver todas la propiedades del 'dict'
print(type(product))         #<class 'dict'>
print(type(person))         #<class 'dict'>

print(person.keys())         #dict_keys(['First_name', 'Last_name'])
print(person.items())        #dict_items([('First_name', 'Fabricio'), ('Last_name', '  Gutierrez')])
# del person                 #Para eliminar todo un elemento
print(person)

product = [
    {"name": 'book', "price": 10.99},
    {"name": 'laptop', "price": 1000}
] #Diccionario dentro de una lista "[]"
print(product)             #[{'name': 'book', 'price': 10.99}, {'name': 'laptop', 'price': 1000}]
print(type(product))       #<<clas 'list'>>