import math
from random import randint

for i in range (10):
    nm = randint (1,50)
    fat=math.factorial(nm)
    print("O número {}, tem o fatorial igual a {}".format(nm,fat))
