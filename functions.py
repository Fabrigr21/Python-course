def hello(): #"def" para crear un funcion (definicion de funcion)
    print("HELLO WORLD")
    
hello()

def hi(name="Person"):
    print("Hello " + name)

hi("joe")
hi("ryan")
hi("stefano")
hi()                    #Cuando no ponemos datos de selecciona como Person
#HELLO WORLD
#Hello joe
#Hello ryan
#Hello stefano
#Hello Person

def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(10, 30))
print(add(600, 10))
print(len("Hello"))     #"5"; ya que cuenta todos los caracteres"1h, 2e, 3l, 4l, 5o"
#lo mismo
add = lambda numberOne, numberTwo: numberOne + numberTwo
print(add(10, 30))