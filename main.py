from determinist import *
from randomWS import *

print("coucou")


ws = multiRand(4,10000)

ws.display()
ws.updateBest()
print(ws.getMax())
