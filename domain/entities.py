class Ship(object):
    def __init__(self,c1,l1,c2,l2,c3,l3):
        self._c1 = c1
        self._l1 = l1
        self._c2 = c2
        self._l2 = l2
        self._c3 = c3
        self._l3 = l3

    def getC1(self):
        return self._c1

    def getC2(self):
        return self._c2

    def getC3(self):
        return self._c3

    def getL1(self):
        return self._l1

    def getL2(self):
        return self._l2

    def getL3(self):
        return self._l3