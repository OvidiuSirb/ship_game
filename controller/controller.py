from domain.entities import  Ship

class Controller:
    def __init__(self,repository):
        self._repo = repository
        self._r0 = [".",".",".",".",".","."]
        self._r1 = [".",".",".",".",".","."]
        self._r2 = [".",".",".",".",".","."]
        self._r3 = [".",".",".",".",".","."]
        self._r4 = [".",".",".",".",".","."]
        self._r5 = [".",".",".",".",".","."]

    def getR0(self):
        return self._r0

    def getR1(self):
        return self._r1

    def getR2(self):
        return self._r1

    def getR3(self):
        return self._r1

    def getR4(self):
        return self._r1

    def getR5(self):
        return self._r5


    def add_ship(self,c1,l1,c2,l2,c3,l3):
        ship = Ship (c1,l1,c2,l2,c3,l3)
        if c1 != "A" and c1 != "B" and c1 != "C" and c1 != "D" and c1 != "E" and c1 != "F":
            raise ValueError("Invalid placement")
        if c3 != "A" and c3 != "B" and c3 != "C" and c3 != "D" and c3 != "E" and c3 != "F":
            raise ValueError("Invalid placement")
        if c2 != "A" and c2 != "B" and c2 != "C" and c2 != "D" and c2 != "E" and c2 != "F":
            raise ValueError("Invalid placement")
        if l1 != "0" and l1 != "1" and l1 != "2" and l1 != "3" and l1 != "4" and l1 != "5":
            raise ValueError("Invalid placement")
        if l2 != "0" and l2 != "1" and l2 != "2" and l2 != "3" and l2 != "4" and l2 != "5":
            raise ValueError("Invalid placement")
        if l3 != "0" and l3 != "1" and l3 != "2" and l3 != "3" and l3 != "4" and l3 != "5":
            raise ValueError("Invalid placement")
        if (c1 != c2 and l1 != l2):
            raise ValueError("Invalid placement")
        self._repo.add_ship(ship)

    def player_board(self,c1,l1,c2,l2,c3,l3):
        if l1 == "0":
            if c1 == "A":
                self._r0[0] = "+"
            if c1 == "B":
                self._r0[1] = "+"
            if c1 == "C":
                self._r0[2] = "+"
            if c1 == "D":
                self._r0[3] = "+"
            if c1 == "E":
                self._r0[4] = "+"
            if c1 == "F":
                self._r0[5] = "+"
        if l1 == "1":
            if c1 == "A":
                self._r1[0] = "+"
            if c1 == "B":
                self._r1[1] = "+"
            if c1 == "C":
                self._r1[2] = "+"
            if c1 == "D":
                self._r1[3] = "+"
            if c1 == "E":
                self._r1[4] = "+"
            if c1 == "F":
                self._r1[5] = "+"
        if l1 == "2":
            if c1 == "A":
                self._r2[0] = "+"
            if c1 == "B":
                self._r2[1] = "+"
            if c1 == "C":
                self._r2[2] = "+"
            if c1 == "D":
                self._r2[3] = "+"
            if c1 == "E":
                self._r2[4] = "+"
            if c1 == "F":
                self._r2[5] = "+"
        if l1 == "3":
            if c1 == "A":
                self._r3[0] = "+"
            if c1 == "B":
                self._r3[1] = "+"
            if c1 == "C":
                self._r3[2] = "+"
            if c1 == "D":
                self._r3[3] = "+"
            if c1 == "E":
                self._r3[4] = "+"
            if c1 == "F":
                self._r3[5] = "+"
        if l1 == "4":
            if c1 == "A":
                self._r4[0] = "+"
            if c1 == "B":
                self._r4[1] = "+"
            if c1 == "C":
                self._r4[2] = "+"
            if c1 == "D":
                self._r4[3] = "+"
            if c1 == "E":
                self._r4[4] = "+"
            if c1 == "F":
                self._r4[5] = "+"
        if l1 == "5":
            if c1 == "A":
                self._r5[0] = "+"
            if c1 == "B":
                self._r5[1] = "+"
            if c1 == "C":
                self._r5[2] = "+"
            if c1 == "D":
                self._r5[3] = "+"
            if c1 == "E":
                self._r5[4] = "+"
            if c1 == "F":
                self._r5[5] = "+"
        if l2 == "0":
            if c2 == "A":
                self._r0[0] = "+"
            if c2 == "B":
                self._r0[1] = "+"
            if c2 == "C":
                self._r0[2] = "+"
            if c2 == "D":
                self._r0[3] = "+"
            if c2 == "E":
                self._r0[4] = "+"
            if c2 == "F":
                self._r0[5] = "+"
        if l2 == "1":
            if c2 == "A":
                self._r1[0] = "+"
            if c2 == "B":
                self._r1[1] = "+"
            if c2 == "C":
                self._r1[2] = "+"
            if c2 == "D":
                self._r1[3] = "+"
            if c2 == "E":
                self._r1[4] = "+"
            if c2 == "F":
                self._r1[5] = "+"
        if l2 == "2":
            if c2 == "A":
                self._r2[0] = "+"
            if c2 == "B":
                self._r2[1] = "+"
            if c2 == "C":
                self._r2[2] = "+"
            if c2 == "D":
                self._r2[3] = "+"
            if c2 == "E":
                self._r2[4] = "+"
            if c2 == "F":
                self._r2[5] = "+"
        if l2 == "3":
            if c2 == "A":
                self._r3[0] = "+"
            if c2 == "B":
                self._r3[1] = "+"
            if c2 == "C":
                self._r3[2] = "+"
            if c2 == "D":
                self._r3[3] = "+"
            if c2 == "E":
                self._r3[4] = "+"
            if c2 == "F":
                self._r3[5] = "+"
        if l2 == "4":
            if c2 == "A":
                self._r4[0] = "+"
            if c2 == "B":
                self._r4[1] = "+"
            if c2 == "C":
                self._r4[2] = "+"
            if c2 == "D":
                self._r4[3] = "+"
            if c2 == "E":
                self._r4[4] = "+"
            if c2 == "F":
                self._r4[5] = "+"
        if l2 == "5":
            if c2 == "A":
                self._r5[0] = "+"
            if c2 == "B":
                self._r5[1] = "+"
            if c2 == "C":
                self._r5[2] = "+"
            if c2 == "D":
                self._r5[3] = "+"
            if c2 == "E":
                self._r5[4] = "+"
            if c2 == "F":
                self._r5[5] = "+"
        if l3 == "0":
            if c3 == "A":
                self._r0[0] = "+"
            if c3 == "B":
                self._r0[1] = "+"
            if c3 == "C":
                self._r0[2] = "+"
            if c3 == "D":
                self._r0[3] = "+"
            if c3 == "E":
                self._r0[4] = "+"
            if c3 == "F":
                self._r0[5] = "+"
        if l3 == "1":
            if c3 == "A":
                self._r1[0] = "+"
            if c3 == "B":
                self._r1[1] = "+"
            if c3 == "C":
                self._r1[2] = "+"
            if c3 == "D":
                self._r1[3] = "+"
            if c3 == "E":
                self._r1[4] = "+"
            if c3 == "F":
                self._r1[5] = "+"
        if l3 == "2":
            if c3 == "A":
                self._r2[0] = "+"
            if c3 == "B":
                self._r2[1] = "+"
            if c3 == "C":
                self._r2[2] = "+"
            if c3 == "D":
                self._r2[3] = "+"
            if c3 == "E":
                self._r2[4] = "+"
            if c3 == "F":
                self._r2[5] = "+"
        if l3 == "3":
            if c3 == "A":
                self._r3[0] = "+"
            if c3 == "B":
                self._r3[1] = "+"
            if c3 == "C":
                self._r3[2] = "+"
            if c3 == "D":
                self._r3[3] = "+"
            if c3 == "E":
                self._r3[4] = "+"
            if c3 == "F":
                self._r3[5] = "+"
        if l3 == "4":
            if c3 == "A":
                self._r4[0] = "+"
            if c3 == "B":
                self._r4[1] = "+"
            if c3 == "C":
                self._r4[2] = "+"
            if c3 == "D":
                self._r4[3] = "+"
            if c3 == "E":
                self._r4[4] = "+"
            if c3 == "F":
                self._r4[5] = "+"
        if l3 == "5":
            if c3 == "A":
                self._r5[0] = "+"
            if c3 == "B":
                self._r5[1] = "+"
            if c3 == "C":
                self._r5[2] = "+"
            if c3 == "D":
                self._r5[3] = "+"
            if c3 == "E":
                self._r5[4] = "+"
            if c3 == "F":
                self._r5[5] = "+"