# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

<<<<<<< HEAD
logger("aloitetaan ohjelma")
=======
logger("aloitetaan ohjelma") # muutos mainissa
>>>>>>> main

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"Lukujen {x} ja {y} summa on {summa(x, y)}")  # muutos bugikorjaus-branchissa
print(f"Lukujen {x} ja {y} erotus on {erotus(x, y)}")  # muutos bugikorjaus-branchissa

logger("lopetetaan ohjelma")
<<<<<<< HEAD
print("goodbye!")
=======
>>>>>>> main
