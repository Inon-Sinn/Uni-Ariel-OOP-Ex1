import Classes
from Classes import CallforElevator as cl
import Block as blk


def add(call: cl, block_list: list):
    c_place = add_call_time(call.time, block_list)
    src_place = add_stop(call.src, c_place, block_list, False)
    dest_place = add_stop(call.dest, src_place, block_list, True)
    add_people(c_place, dest_place)


def add_call_time(time, block_list):
    return 0


def add_stop(place, last_place, block_list, dest_bool):
    return 0


def add_people(call_place, dest_place):
    print("hi")

def total_time_calculator(blocklist):
    return 0

class Allocation:

    def __init__(self, building, call_list):
        self.building = building
        self.call_list = call_list
        self.total_time = 0  # helper
        self.total_List = list()
        self.allocation = list()
        self.total_time_list = list()

        default_block = blk()
        for i in range(building.getNumofElevators()):  # check if its working
            self.total_List.append([])
        for i in self.total_List:
            i.append(default_block)

        for i in range(building.getNumofElevators()):  # check if its working
            self.total_time_list.append(0)

        for c in call_list:
            self.allocation.append(self.allocate_call(c))

    def update_total_time(self, time):
        self.total_time += time

    def allocate_call(self, call):
        temporary_total_time_List = list()
        for elev in range(len(self.total_List)):  # goes to over the elvetors for the calculation
            list_copy = self.total_List[elev].copy()
            add(call, list_copy)
            total_time = 0
            for block in list_copy:
                total_time += block.total_time
            temporary_total_time_List.append(total_time - self.total_time_list[elev])

        min = temporary_total_time_List[0]  # Calculate which is the best choose
        ans = 0
        for i in range(len(temporary_total_time_List)):
            if min > temporary_total_time_List[i]:
                min = temporary_total_time_List[i]
                ans = i

        self.total_time_list[ans] += min  # Update the new choose
        self.update_total_time(temporary_total_time_List[ans])
        add(call, self.total_List[ans])
        return ans
