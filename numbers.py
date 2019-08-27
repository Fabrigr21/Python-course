print(type(9))      #<class 'int'>
print(type(10.1))   #<class 'float'>
                # 2**3 = 8
                # 3%2 = 1 
age = input("Insert your age:") # ("10" o '0', no son numeros)
print(age)                      #Todo lo que agregamos es un string

print(type(float(age)))      #si cambio a "float", por "int" puedo cambiar su class 
new_age = int(age) + 5
print(new_age)
