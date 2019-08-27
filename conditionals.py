
x = 31
if x < 30:
    print("x is less than 30")           #si es menor
else:
    print("x is greater than 30")        #si es mayor

y = 30
if y == 30:
    print("y is 30")
else:
    print("y isn't 30")

color = "yellow"
if color == "red":
    print("the color is red")          #si es == red 
elif color == "blue":
    print("the color is blue")         #si no es red es blue
elif color == "yellow":
    print("the color is yellow")
else:
    print("any color")                 #si no es == red ni blue 

#-----COMPLETAR 

if x > 2:
    if x < 10:
        print()

if x > 2 and x <= 10:   #and, or, not 
    print("x is greater than two and less than or equal to ten")
else:
    print("x isn't greater")
if x > 2 or x <= 20:
    print("x is geater than two or less or equal to twenty")
if x > 2 or x <=30:
    print("x is geater than two or less equal to theerty")
if(not(x == y)):
    print("x is not equal y")

print(x)
print(y)

