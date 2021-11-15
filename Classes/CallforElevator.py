class CallforElevator:
    def __init__(self, state, time, src, dest, type, allocated_to):
        self.state = state
        self.time = time
        self.src = src
        self.dest = dest
        self.type = type
        self.allocated_to = allocated_to

    def getState(self):
        return self.state

    def getTime(self):
        return self.time

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def getType(self):
        return self.type

    def getAllocation(self):
        return self.allocated_to
