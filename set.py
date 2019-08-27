#definir a una conecxion que no tiene un indice y es desordenada
 
colors = {
    'Red','Green', 'Blue'
    }
print(type(colors))                  #<class 'set'>
print(colors)
print('Red' in colors)               #True
colors.add('violet')                 #agrega 'violet'
print(colors)                        #{'Blue', 'Red', 'Green', 'violet'} 

colors.remove('Red')
print(colors)                        #{'violet', 'Blue', 'Green'}

colors.clear()                       #Una funcion para <list>
print(colors)                        #set()
                                     #Para convertir en comentario: "crtl+(k+crtl)+c"
