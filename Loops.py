foods = ['apples', 'bread', 'cheese', 'milk', 'bananas']

print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])
print(foods[4])
# Lo de arriba y lo de abajo es lo mismo.
for food in foods:
    if food == "cheese":
        print("you have to buy this")
    if food == "milk":
        #break               #Cuando llega al elemento milk ya no continua
        continue           #Cuando llega al elemento milk no lo ejecuta, pero continua
    print(food)

for number in range(1,8):
    print(number)

for letter in "Hello":
    print(letter)

count = 4

while count <= 10:
    print(count)
    count = count + 1