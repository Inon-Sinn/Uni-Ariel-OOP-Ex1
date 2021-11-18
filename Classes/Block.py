class Block:
    def __init__(self,call_time: bool = False, type: int = 0, time: int = 0, place: int = 0, people: int = 0, going_out_bool: bool = False):
        self.call_time = call_time
        self.type = type  # need something for impossible
        self.time = time
        self.place = place
        self.people = people
        self.going_out_bool = going_out_bool
