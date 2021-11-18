from Classes.CallforElevator import CallforElevator as cl
from Classes.Block import Block as blk


def add(call: cl, block_list: list):
    c_place = add_call_time(call.time, block_list)
    src_place = add_stop(call.src, c_place, block_list, False)
    dest_place = add_stop(call.dest, src_place, block_list, True)
    add_people(c_place, dest_place, block_list)


def add_call_time(time, block_list):
    return 0


def add_stop(place, last_place, block_list, dest_bool):
    return 0


def add_people(call_place, dest_place, block_list):
    for i in range(call_place, dest_place):  # Not including dest_place so check it works!
        block_list[i].people += 1


def total_time_calculator(blocklist):
    total_time = 0
    for i in range(len(blocklist) - 1):  # with work with next so i want 'i' to only got up to one before the last
        time = blocklist[i + 1].time - blocklist[i].time
        time = time * blocklist[i].people
        total_time += time
    return total_time


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
            total_time = total_time_calculator(list_copy)
            temporary_total_time_List.append(total_time - self.total_time_list[elev])
        min = temporary_total_time_List[0]  # Calculate which is the best choose
        ans = 0
        for i in range(len(temporary_total_time_List)):
            if min > temporary_total_time_List[i]:
                min = temporary_total_time_List[i]
                ans = i
        self.total_time_list[ans] += min  # Update the new choose
        self.update_total_time(min)
        add(call, self.total_List[ans])
        return ans
