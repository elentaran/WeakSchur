from weakSchur import *
import random

def getPossibilities(ws,elem):
    posBin = []
    for i in range(ws.getNbBin()):
        if ws.addVerify(elem,i):
            posBin.append(i)
    return posBin


def generateRand(nbBin):
    vals=[]
    for i in range(nbBin):
        vals.append([])

    ws = WeakSchur(vals)
    elem = 1

    posBin = getPossibilities(ws,elem)
    while len(posBin) > 0:
        chosenBin = choseBin3(posBin)
        ws.addElem(elem,chosenBin)
        elem+=1
        posBin = getPossibilities(ws,elem)
    return ws

def multiRand(nbBin,nbTry):
    bestVal = 0
    bestWS = WeakSchur([[]])
    for i in range(nbTry):
        ws = generateRand(nbBin)
        if ws.getMax() > bestVal:
            bestVal = ws.getMax()
            bestWS = ws
    return bestWS

def choseBin(posBin):
    chosenBin = posBin[random.randint(0,len(posBin)-1)]
    return chosenBin

def choseBin2(posBin):
    chosenBin = posBin[0]
    return chosenBin

def choseBin3(posBin):
    if (len(posBin) == 1):
        return posBin[0]
    else:
        ran = random.uniform(0,1)
        if ran < 0.9:
            return posBin[0]
        else :
            return posBin[1]
