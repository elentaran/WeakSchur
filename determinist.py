from weakSchur import *

def createDeterministWS(nbBin):
    if nbBin == 1:
        return [[1,2]]
    else:
        valsNm1 = createDeterministWS(nbBin-1)

    wsNm1 = WeakSchur(valsNm1)
    bestNm1 = wsNm1.getMax()
    listNew = createSeq(bestNm1+1,1)
    valsN = valsNm1+[listNew]
    return valsN

def createSeq(firstVal,hole=0):
    seq=[]
    seq.append(firstVal)
    if hole==0:
        for i in range(firstVal+1,2*(firstVal)+1):
            seq.append(i)
    elif hole==1:
        for i in range(firstVal+2,2*(firstVal)+2):
            seq.append(i)
    return seq



