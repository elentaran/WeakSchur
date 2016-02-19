from determinist import *
from deterministSchur import *
from randomWS import *

print("coucou")

"""
ws = multiRand(4,10000)

ws.display()
ws.updateBest()
print(ws.getMax())
"""

ws = WeakSchur(createDeterministS(8))
print(ws.verify())
#ws.display()
print(ws.getMax())
