class Block:
    def __init__(self,elev_place, src, dest, total_time, call_time):
        self.elev_place = elev_place # need something for impossible
        self.src = [src]
        self.dest = [dest]
        self.total_time = total_time
        self.call_time = call_time

    def merge(self):
        print("merges two blockes which are not indepedent")
