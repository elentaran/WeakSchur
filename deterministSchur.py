from weakSchur import *

def createDeterministS(nbBin):
    if nbBin == 1:
        return [[1]]
    else:
        valsNm1 = createDeterministS(nbBin-1)

    " Add last line "
    wsNm1 = WeakSchur(valsNm1)
    previousBest = wsNm1.getMax()
    listNew = createLastLine(previousBest)
    valsN = valsNm1+[listNew]

    " Complete other lines "
    maxVal = 3*previousBest+1
    for i in range(len(valsN)-1):
        newVals = getReverse(valsN[i],maxVal)
        valsN[i]=valsN[i]+newVals

    return valsN


def createLastLine(previousBest):
    seq=[]
    for i in range(previousBest+1,2*previousBest+2):
        seq.append(i)
    return seq

def getReverse(vals,maxVal):
    seq=[]
    for i in vals:
        seq.append(maxVal+1-i)
    seq.reverse()
    return seq


