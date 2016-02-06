class WeakSchur:
    vals = [[]]

    def __init__(self,vals):
        self.vals = vals


    def load(self,nameFile):
        self.vals=[]
        with open(nameFile) as myFile:
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


    def verify(self):
        for oneBin in self.vals:
            oneBin.sort()
            for i in range(len(oneBin)):
                for j in range(i):
                    for l in range(j+1,i):
                        if oneBin[j] + oneBin[l] == oneBin[i]:
                            return False

        return True

    def display(self):
        for i in self.vals:
            print(i)

