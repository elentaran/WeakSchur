from weakSchur import *

def createDeterministWS(nbBin):
    if nbBin == 1:
        return [[1,2]]
    else:
        valsM1 = createDeterministWS(nbBin-1)

    listNew=[]
    

