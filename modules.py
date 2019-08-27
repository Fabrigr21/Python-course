# own modules (modulo propio)
# thirdy party modules (modulo descargado "web")
# python modules (modulos de python)

#---------------
import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes=70))
print(datetime.timedelta(minutes=100))

# lo de abajo es lo mismo 

from datetime import timedelta,date 

print(timedelta(minutes=100))
print(date.today())

#-------------------

import mymMath
mymMath.add(1,2)             #"3", utilizando la formula de mymMath(propia)
mymMath.substract(1,2)

# Lo de arriba y abajo es lo mismo 
from mymMath import add,substract

substract(1,2)
add(1,2)

#--------------------
 
from colorama import Fore, Style, init  #pypi pip install colorama
init(convert=True)
print(Fore.RED + "Hello World")
 