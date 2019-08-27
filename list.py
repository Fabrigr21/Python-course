demo_list =[1, 'hello', 1.34, True,[1, 2, 3]]
colors = ['red', 'green', 'blue']

numbers_list = list((1, 2, 3, 4))   #Uso una tupla que generar 1 variable en vez de 4 
print(numbers_list)
print(type(numbers_list))           #Tipo de la lista

r = list(range(1, 10))              #Enumera del 1 hasta el 9
print(r)
print(type(colors))                 #Class "List"

#print(dir(colors))                  #"dir" para ver la info (List)
print(len(colors))                  #Para saber la longitud este caso es "3" (solo tiene 3 elementos)
print(colors[1])                    #Para denotar la posicion 1 (green)
print(colors[-1])                   #Blue
print('green'in colors)             #"green esta en colors?"/ true
print("violet" in colors)           #False
print("hello" in demo_list)         #True
print('1' in demo_list)             #False

print(colors)
#colors[1] = 'yellow'                #Cambia una variable
print(colors)                       #Cambia según la úliima alteración

#print(dir(colors))                 #"dir" para ver todos los cambios 

#colors.append('violet')             #Para agregar ['red', 'green, 'blue', 'violet']
#colors.append(('violet', 'yellow'))  #Para agregar ['red', 'green, 'blue', ('violet', 'yellow')]
colors.extend(['violet','yellow']) 
colors.extend(['pink', 'black'])     #['red', 'green', 'blue', 'violet', 'yellow', 'pink', 'black']      
print(colors)                       

colors.insert(-1, 'purple')       
colors.insert(1, 'purple')
print(colors)                         #['red', 'purple', 'green', 'blue', 'violet', 'yellow', 'pink', 'purple', 'black']

colors.insert(len(colors), 'violet')
print(colors)                         #['red', 'purple', 'green', 'blue', 'violet', 'yellow', 'pink', 'purple', 'black', 'violet']    

colors.pop()                          #Para quitar el ultimo elemento
colors.pop()                          #Para quitar los 2 ultimos elementos
print(colors)                         #['red', 'purple', 'green', 'blue', 'violet', 'yellow', 'pink', 'purple']

colors.remove('green')
colors.pop(1)
print(colors)                         #['red', 'blue', 'violet', 'yellow', 'pink', 'purple']

#colors.clear()                        #Para borrar todo los datos 
#print(colors)                          #[]

colors.sort()                          #Los coloca alfabeticamente
print(colors)                          #['blue', 'pink', 'purple', 'red', 'violet', 'yellow']

colors.sort(reverse= True)            #Los coloca al revez del sentiso alfabetico
print(colors)                         #['yellow', 'violet', 'red', 'purple', 'pink', 'blue']

print(colors.index('yellow'))         # '0' ya que comenzo con yellow

colors.insert(1, 'pink')              # Para insertar pink
print(colors)

print(colors.count('pink'))           #cuantas veces se repite 'pink'?, 2 veces 