class CallforElevator:

    #INIT=0, GOING2SRC=1, GOIND2DEST=2, DONE=3; - state
    #UP=1, DOWN=-1; - type
    def __init__(self, time, src, dest, state, allocated_to):
        self.state = int(state)
        self.time = float(time)
        self.src = int(src)
        self.dest = int(dest)
        if self.dest - self.src > 0:
            self.type = 1
        else:
            self.type = -1
        self.allocated_to = int(allocated_to)

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

    def __str__(self):
        return "state:{state} time:{time} src:{src} dest:{dest} type:{type} acllocated_to:{allo}\n".format(state=self.state,time=self.time,src=self.src,dest=self.dest,type=self.type,allo=self.allocated_to)

    def __repr__(self):
        return "state:{state} time:{time} src:{src} dest:{dest} type:{type} acllocated_to:{allo}\n".format(state=self.state,time=self.time,src=self.src,dest=self.dest,type=self.type,allo=self.allocated_to)
