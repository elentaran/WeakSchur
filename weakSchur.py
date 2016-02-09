class WeakSchur:
    vals = [[]]
    fileBest = "highscores/ws"

    def __init__(self,vals):
        self.vals = vals


    def load(self,nameFile):
        self.vals=[]
        try:
            with open(nameFile,mode='rt') as myFile:
                lines=myFile.read().split("\n")
                for line in lines:
                    if line != "":
                        valstext = line.split(" ")
                        valsline = []
                        for val in valstext:
                            if val != "":
                                valsline.append(int(val))
                        self.vals.append(sorted(valsline))
            print("weak schur loaded")
        except FileNotFoundError:
            print("inexisting file")

        if not(self.verify()):
            print("warning: invalid weak schur")
        return


    def save(self,nameFile):
        with open(nameFile,mode='wt') as myFile:
            for i in self.vals:
                for j in i:
                    myFile.write(str(j)+" ")
                myFile.write("\n")
        print("weak schur saved")
        return

    def updateBest(self):
        best = WeakSchur([[]])
        best.load(self.fileBest+str(self.getNbBin()))
        bestVal = best.getMax()
        if self.getMax() > bestVal:
            print(" new Highscore! " + str(self.getMax()))
            self.save(self.fileBest+str(self.getNbBin()))
        return


    def verify(self):
        res=[]
        for oneBin in self.vals:
            res+=oneBin
        res.sort()
        for i in range(1,len(res)+1):
            if res[i-1] != i:
                return False

        for oneBin in self.vals:
            oneBin.sort()
            for i in range(len(oneBin)):
                for j in range(i):
                    for l in range(j+1,i):
                        if oneBin[j] + oneBin[l] == oneBin[i]:
                            return False
        return True


    def addElem(self,elem,numBin):
        self.vals[numBin].append(elem)

    def addVerify(self,elem,numBin):
        oneBin = self.vals[numBin]
        for i in range(len(oneBin)):
            for j in range(i):
                if oneBin[i] + oneBin[j] == elem:
                    return False
        return True

    def getMax(self):
        res=[]
        for oneBin in self.vals:
            res+=oneBin
        return len(res)

    def getNbBin(self):
        return len(self.vals)

    def display(self):
        for i in self.vals:
            print(i)

