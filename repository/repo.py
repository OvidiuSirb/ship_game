class Repo:
    def __init__(self):
        self._data = []
        self._backup = []
        self._r0 = [".", ".", ".", ".", ".", "."]
        self._r1 = [".", ".", ".", ".", ".", "."]
        self._r2 = [".", ".", ".", ".", ".", "."]
        self._r3 = [".", ".", ".", ".", ".", "."]
        self._r4 = [".", ".", ".", ".", ".", "."]
        self._r5 = [".", ".", ".", ".", ".", "."]


    def add_ship(self,obj):
        self._backup = self._data.copy()
        self._data.append(obj)
        self.player_board()

    def getAll(self):
        return (self._data,self._backup)

    def getR0(self):
        return self._r0

    def getR1(self):
        return self._r1

    def getR2(self):
        return self._r2

    def getR3(self):
        return self._r3

    def getR4(self):
        return self._r4

    def getR5(self):
        return self._r5

    def player_board(self):
        if len(self._data )==1:
            if self._data[len(self._data)-1].getL1 == "0":
                if self._data[len(self._data)-1].getC1 == "A":
                    self._r0[0] = "+"
                if self._data[len(self._data)-1].getC1 == "B":
                    self._r0[1] = "+"
                if self._data[len(self._data)-1].getC1 == "C":
                    self._r0[2] = "+"
                if self._data[len(self._data)-1].getC1 == "D":
                    self._r0[3] = "+"
                if self._data[len(self._data)-1].getC1 == "E":
                    self._r0[4] = "+"
                if self._data[len(self._data)-1].getC1 == "F":
                    self._r0[5] = "+"
            if self._data[len(self._data)-1].getL1 == "1":
                if self._data[len(self._data)-1].getC1 == "A":
                    self._r1[0] = "+"
                if self._data[len(self._data)-1].getC1 == "B":
                    self._r1[1] = "+"
                if self._data[len(self._data)-1].getC1 == "C":
                    self._r1[2] = "+"
                if self._data[len(self._data)-1].getC1 == "D":
                    self._r1[3] = "+"
                if self._data[len(self._data)-1].getC1 == "E":
                    self._r1[4] = "+"
                if self._data[len(self._data)-1].getC1 == "F":
                    self._r1[5] = "+"
            if self._data[len(self._data)-1].getL1 == "2":
                if self._data[len(self._data)-1].getC1 == "A":
                    self._r2[0] = "+"
                if self._data[len(self._data)-1].getC1 == "B":
                    self._r2[1] = "+"
                if self._data[len(self._data)-1].getC1 == "C":
                    self._r2[2] = "+"
                if self._data[len(self._data)-1].getC1 == "D":
                    self._r2[3] = "+"
                if self._data[len(self._data)-1].getC1 == "E":
                    self._r2[4] = "+"
                if self._data[len(self._data)-1].getC1 == "F":
                    self._r2[5] = "+"
            if self._data[len(self._data)-1].getL1 == "3":
                if self._data[len(self._data)-1].getC1 == "A":
                    self._r3[0] = "+"
                if self._data[len(self._data)-1].getC1 == "B":
                    self._r3[1] = "+"
                if self._data[len(self._data)-1].getC1 == "C":
                    self._r3[2] = "+"
                if self._data[len(self._data)-1].getC1 == "D":
                    self._r3[3] = "+"
                if self._data[len(self._data)-1].getC1 == "E":
                    self._r3[4] = "+"
                if self._data[len(self._data)-1].getC1 == "F":
                    self._r3[5] = "+"
            if self._data[len(self._data)-1].getL1 == "4":
                if self._data[len(self._data)-1].getC1 == "A":
                    self._r4[0] = "+"
                if self._data[len(self._data)-1].getC1 == "B":
                    self._r4[1] = "+"
                if self._data[len(self._data)-1].getC1 == "C":
                    self._r4[2] = "+"
                if self._data[len(self._data)-1].getC1 == "D":
                    self._r4[3] = "+"
                if self._data[len(self._data)-1].getC1 == "E":
                    self._r4[4] = "+"
                if self._data[len(self._data)-1].getC1 == "F":
                    self._r4[5] = "+"
            if self._data[len(self._data)-1].getL1 == "5":
                if self._data[len(self._data)-1].getC1 == "A":
                    self._r5[0] = "+"
                if self._data[len(self._data)-1].getC1 == "B":
                    self._r5[1] = "+"
                if self._data[len(self._data)-1].getC1 == "C":
                    self._r5[2] = "+"
                if self._data[len(self._data)-1].getC1 == "D":
                    self._r5[3] = "+"
                if self._data[len(self._data)-1].getC1 == "E":
                    self._r5[4] = "+"
                if self._data[len(self._data)-1].getC1 == "F":
                    self._r5[5] = "+"
            if self._data[len(self._data)-1].getL2 == "0":
                if self._data[len(self._data)-1].getC2 == "A":
                    self._r0[0] = "+"
                if self._data[len(self._data)-1].getC2 == "B":
                    self._r0[1] = "+"
                if self._data[len(self._data)-1].getC2 == "C":
                    self._r0[2] = "+"
                if self._data[len(self._data)-1].getC2 == "D":
                    self._r0[3] = "+"
                if self._data[len(self._data)-1].getC2 == "E":
                    self._r0[4] = "+"
                if self._data[len(self._data)-1].getC2 == "F":
                    self._r0[5] = "+"
            if self._data[len(self._data)-1].getL2 == "1":
                if self._data[len(self._data)-1].getC2 == "A":
                    self._r1[0] = "+"
                if self._data[len(self._data)-1].getC2 == "B":
                    self._r1[1] = "+"
                if self._data[len(self._data)-1].getC2 == "C":
                    self._r1[2] = "+"
                if self._data[len(self._data)-1].getC2 == "D":
                    self._r1[3] = "+"
                if self._data[len(self._data)-1].getC2 == "E":
                    self._r1[4] = "+"
                if self._data[len(self._data)-1].getC2 == "F":
                    self._r1[5] = "+"
            if self._data[len(self._data)-1].getL2 == "2":
                if self._data[len(self._data)-1].getC2 == "A":
                    self._r2[0] = "+"
                if self._data[len(self._data)-1].getC2 == "B":
                    self._r2[1] = "+"
                if self._data[len(self._data)-1].getC2 == "C":
                    self._r2[2] = "+"
                if self._data[len(self._data)-1].getC2 == "D":
                    self._r2[3] = "+"
                if self._data[len(self._data)-1].getC2 == "E":
                    self._r2[4] = "+"
                if self._data[len(self._data)-1].getC2 == "F":
                    self._r2[5] = "+"
            if self._data[len(self._data)-1].getL2 == "3":
                if self._data[len(self._data)-1].getC2 == "A":
                    self._r3[0] = "+"
                if self._data[len(self._data)-1].getC2 == "B":
                    self._r3[1] = "+"
                if self._data[len(self._data)-1].getC2 == "C":
                    self._r3[2] = "+"
                if self._data[len(self._data)-1].getC2 == "D":
                    self._r3[3] = "+"
                if self._data[len(self._data)-1].getC2 == "E":
                    self._r3[4] = "+"
                if self._data[len(self._data)-1].getC2 == "F":
                    self._r3[5] = "+"
            if self._data[len(self._data)-1].getL2 == "4":
                if self._data[len(self._data)-1].getC2 == "A":
                    self._r4[0] = "+"
                if self._data[len(self._data)-1].getC2 == "B":
                    self._r4[1] = "+"
                if self._data[len(self._data)-1].getC2 == "C":
                    self._r4[2] = "+"
                if self._data[len(self._data)-1].getC2 == "D":
                    self._r4[3] = "+"
                if self._data[len(self._data)-1].getC2 == "E":
                    self._r4[4] = "+"
                if self._data[len(self._data)-1].getC2 == "F":
                    self._r4[5] = "+"
            if self._data[len(self._data)-1].getL2 == "5":
                if self._data[len(self._data)-1].getC2 == "A":
                    self._r5[0] = "+"
                if self._data[len(self._data)-1].getC2 == "B":
                    self._r5[1] = "+"
                if self._data[len(self._data)-1].getC2 == "C":
                    self._r5[2] = "+"
                if self._data[len(self._data)-1].getC2 == "D":
                    self._r5[3] = "+"
                if self._data[len(self._data)-1].getC2 == "E":
                    self._r5[4] = "+"
                if self._data[len(self._data)-1].getC2 == "F":
                    self._r5[5] = "+"
            if self._data[len(self._data)-1].getL3 == "0":
                if self._data[len(self._data)-1].getC3 == "A":
                    self._r0[0] = "+"
                if self._data[len(self._data)-1].getC3 == "B":
                    self._r0[1] = "+"
                if self._data[len(self._data)-1].getC3 == "C":
                    self._r0[2] = "+"
                if self._data[len(self._data)-1].getC3 == "D":
                    self._r0[3] = "+"
                if self._data[len(self._data)-1].getC3 == "E":
                    self._r0[4] = "+"
                if self._data[len(self._data)-1].getC3 == "F":
                    self._r0[5] = "+"
            if self._data[len(self._data)-1].getL3 == "1":
                if self._data[len(self._data)-1].getC3 == "A":
                    self._r1[0] = "+"
                if self._data[len(self._data)-1].getC3 == "B":
                    self._r1[1] = "+"
                if self._data[len(self._data)-1].getC3 == "C":
                    self._r1[2] = "+"
                if self._data[len(self._data)-1].getC3 == "D":
                    self._r1[3] = "+"
                if self._data[len(self._data)-1].getC3 == "E":
                    self._r1[4] = "+"
                if self._data[len(self._data)-1].getC3 == "F":
                    self._r1[5] = "+"
            if self._data[len(self._data)-1].getL3 == "2":
                if self._data[len(self._data)-1].getC3 == "A":
                    self._r2[0] = "+"
                if self._data[len(self._data)-1].getC3 == "B":
                    self._r2[1] = "+"
                if self._data[len(self._data)-1].getC3 == "C":
                    self._r2[2] = "+"
                if self._data[len(self._data)-1].getC3 == "D":
                    self._r2[3] = "+"
                if self._data[len(self._data)-1].getC3 == "E":
                    self._r2[4] = "+"
                if self._data[len(self._data)-1].getC3 == "F":
                    self._r2[5] = "+"
            if self._data[len(self._data)-1].getL3 == "3":
                if self._data[len(self._data)-1].getC3 == "A":
                    self._r3[0] = "+"
                if self._data[len(self._data)-1].getC3 == "B":
                    self._r3[1] = "+"
                if self._data[len(self._data)-1].getC3 == "C":
                    self._r3[2] = "+"
                if self._data[len(self._data)-1].getC3 == "D":
                    self._r3[3] = "+"
                if self._data[len(self._data)-1].getC3 == "E":
                    self._r3[4] = "+"
                if self._data[len(self._data)-1].getC3 == "F":
                    self._r3[5] = "+"
            if self._data[len(self._data)-1].getL3 == "4":
                if self._data[len(self._data)-1].getC3 == "A":
                    self._r4[0] = "+"
                if self._data[len(self._data)-1].getC3 == "B":
                    self._r4[1] = "+"
                if self._data[len(self._data)-1].getC3 == "C":
                    self._r4[2] = "+"
                if self._data[len(self._data)-1].getC3 == "D":
                    self._r4[3] = "+"
                if self._data[len(self._data)-1].getC3 == "E":
                    self._r4[4] = "+"
                if self._data[len(self._data)-1].getC3 == "F":
                    self._r4[5] = "+"
            if self._data[len(self._data)-1].getL3 == "5":
                if self._data[len(self._data)-1].getC3 == "A":
                    self._r5[0] = "+"
                if self._data[len(self._data)-1].getC3 == "B":
                    self._r5[1] = "+"
                if self._data[len(self._data)-1].getC3 == "C":
                    self._r5[2] = "+"
                if self._data[len(self._data)-1].getC3 == "D":
                    self._r5[3] = "+"
                if self._data[len(self._data)-1].getC3 == "E":
                    self._r5[4] = "+"
                if self._data[len(self._data)-1].getC3 == "F":
                    self._r5[5] = "+"