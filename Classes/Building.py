class Building():
    def __init__(self, minFloor, maxFloor, elevList):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.elevList = elevList

    def getMinFloor(self):
        return self.minFloor

    def getMaxFloor(self):
        return self.maxFloor

    def getNumofElevators(self):
        return len(self.elevList)

    def getElevetor(self, elev):
        return self.elevList[elev]

    def __str__(self):
        ans1 = "MinFloor:{min}\nMaxFloor:{max}\n".format(min=self.minFloor, max=self.maxFloor)
        return ans1
