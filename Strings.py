myStr = "Hello World"
#Para ver las propiedades
# #print(dir(myStr))    #"Quitar el '#'para visualizar" <-
# | ctrl + 'k+ctrl' + c = comment

#-----------------------------------------------------------------------------------------
print("Mood " + myStr) #Lo agrupa sin espaciado, por eso uno debe de separarlo con espacio
print(f"Mood {myStr}")   #Mi preferida 
print("Mood {0}".format(myStr))
#-----------------------------------------------------------------------------------------

print(myStr.upper()) #Para que todo el texto este en mayuscula
print(myStr.lower()) #Para que todo el texto este en minuscula
print(myStr.swapcase()) #Lo que antes era Mayuscula cambia Minuscula
print(myStr.capitalize()) #La primera letra del texto es mayuscula 
print(myStr.replace('Hello','Bye')) #Para hacer un cambio de variable
print(myStr.replace('Hello', 'BYE').upper()) #Puedes combinar las variables
print(myStr.count('l')) #Para contar los caracteres, se puede contar los vacios (' ')

print(myStr.startswith('hola')) #Sera cierto que comienza con ('---'), true or false
                                # ->le podria decir que empiza con ('H') o ('He') ambas son correctas
print(myStr.endswith('World')) #Es "True", ya que termina el World

#--------------------------------------------------------------
myStrr = "Hello World car"
print(myStrr.split()) #Separa los caracteres según lo que hemos determinado
print(myStrr.split('o')) #['Hell', 'W', 'orl']
print(myStrr.find('W')) # Es la letra '6', el primer caracter es '0'
#--------------------------------------------------------------

print(len(myStr)) #Cuenta todas las letras, en este caso el primer termino lo cuenta como '1'
print(myStr.index('e')) #Cuenta la 'h' como '0' y la 'e' se determina en '1'

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[4]) #Para denotar el valor que se encuentra en esa posicion 'o', comienza de 0
print(myStr[3]) #'l'
print(myStr[0]) #'H'
print(myStr[-1]) #'d', la ultimo determinando se considera "[-1]"
print(myStr[-3]) #'r'

