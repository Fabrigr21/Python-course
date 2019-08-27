x =(1, 2, 3)
print(type(x))        #<class 'tuple'>

months = ('January', 'Febreary')

y = tuple((1, 2, 3))
print(y)
z=(1)                             

'''print(dir(x))                 #Para ver propiedades de una tupla
print(dir(1))'''                 #Para ver las propiedades de los enteros
print(type(z))                   #<class int>
                                 #Usando ('''.....''') puedes hacer un comentario 
w = (1,)
print(type(w))                   #<class tuples> (colo por pones (1','))
print(w)

t = (1, 2, 3, 4)
print(t[0])                     #'1'
print(t[3])                     #'4' (ya tupla es un valor inmutable x[4] = 10, false)

'''del(t)
print(t)'''

#Uso de tuplas

locations = {
    (35.12312, 39.000) :"Tokyo",
    (35.12312, 39.000) : "New yoir"
}
print(locations)
print(type(locations))          #<class 'dict'>