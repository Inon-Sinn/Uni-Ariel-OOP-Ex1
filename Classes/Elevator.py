class Elevator:
    def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime):
        self.id = id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.startTime = startTime
        self.stopTime = stopTime

    def getID(self):
        return self.id

    def getSpeed(self):
        return self.speed

    def getMinFloor(self):
        return self.minFloor

    def getMaxFloor(self):
        return self.maxFloor

    def getCloseTime(self):
        return self.closeTime

    def getOpenTime(self):
        return self.openTime

    def getStartTime(self):
        return self.startTime

    def getStopTime(self):
        return self.stopTime

    def __str__(self):
        ans1 = "id:{id}\nspeed:{speed}\nminFloor:{min}\nmaxFloor:{max}\n".format(id=self.id, speed=self.speed,
                                                                                min=self.minFloor, max=self.maxFloor)
        ans2 = "closeTime:{close}\nopenTime:{open}\nstartTime{start}\nstopTime:{stop}".format(close=self.closeTime,
                                                                                              open=self.openTime,
                                                                                              start=self.startTime,
                                                                                              stop=self.stopTime)
        return ans1+ans2