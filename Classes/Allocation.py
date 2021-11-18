from Classes.CallforElevator import CallforElevator as cl
from Classes.Block import Block as blk


def add(call: cl, block_list: list, elev):
    stop = elev.closeTime + elev.openTime + elev.startTime + elev.stopTime
    c_place = add_call_time(call.time, block_list, elev.speed)
    src_place = add_stop(call.src, c_place, block_list, False, elev.speed, stop)
    dest_place = add_stop(call.dest, src_place, block_list, True, elev.speed, stop)
    add_people(c_place, dest_place, block_list)


def add_call_time(time, block_list, speed):
    last = len(block_list) - 1
    if block_list[last].time <= time:  # Adding a new block to the end the list
        new_block = blk(True, block_list[last - 1].type, time, block_list[last - 1].place,
                        block_list[last - 1].people + 1)
        block_list.append(new_block)
        return last + 1

    for i in range(len(block_list) - 1):  # Inserting the block somewhere in between
        if block_list[i].time <= time <= block_list[i + 1].time:
            new_place = block_list[i].place  # block_list[i].place + (time-block_list[i].time) UNFINISHED
            if block_list[i].place < block_list[i + 1].place:
                new_place += (time - block_list[i]) * speed
            else:
                if block_list[i].place > block_list[i + 1].place:
                    new_place -= (time - block_list[i]) * speed
            new_block2 = blk(True, block_list[i].type, time, new_place, block_list[i].people + 1)
            block_list.insert(i + 1, new_block2)
            return i + 1
    return 0


def add_stop(place, last_place, block_list, dest_bool, speed, stop):  # UNFINISHED
    if last_place == len(block_list) - 1:
        calc = calc_time(last_place, place, speed)
        if dest_bool:  # for when we are adding a destination and not the src
            block_list.append(blk(False, block_list[last_place].type, block_list[last_place].time + calc, place,
                                  block_list[last_place].people))
            block_list.append(blk(False, block_list[last_place].type, block_list[last_place].time + calc + stop, place,
                                  block_list[last_place].people))
            block_list.append(
                blk(False, 0, block_list[last_place].time + calc + stop, place, block_list[last_place].people - 1,
                    True))
        else:  # for when we are adding a source
            ty_src = calc_type(block_list[last_place].place, place)
            block_list.append(
                blk(False, ty_src, block_list[last_place].time + calc, place, block_list[last_place].people))
            block_list.append(
                blk(False, ty_src, block_list[last_place].time + calc + stop, place, block_list[last_place].people))
        return last_place + 1
    for i in range(len(block_list) - 1):
        if (block_list[i].place == place == block_list[i + 1].place) & (
                block_list[i + 1].going_out_bool):  # People going in or out at the same place
            if dest_bool:
                block_list[i + 1].people -= 1
            else:  # only count time for uploading
                block_list.insert(i + 1,
                                  blk(block_list[i].type, block_list[i].time + stop, place, block_list[i].people))
                update_list(i + 1, block_list, stop, speed)
            return i + 1
        if (block_list[i].place <= place < block_list[i + 1].place) | (
                block_list[i].place >= place > block_list[i + 1].place):
            calc = calc_time(block_list[i].place, place, speed)
            block_list.insert(i + 1,
                              blk(False, block_list[i].type, block_list[i].time + calc, place, block_list[i].people))
            block_list.insert(i + 2, blk(False, block_list[i].type, block_list[i].time + calc + stop, place,
                                         block_list[i].people))
            update_list(i + 2, block_list, stop, speed)
            return i + 2
        tp = calc_type(block_list[i + 1].place, place)
        if (block_list[i + 1].type == 0) & ((block_list[i].type == tp) | (
                tp == 0)):  # check for the thing with two people of the entering and going for the same place
            block_list[i + 1].type = block_list[i].type
            calc = calc_time(block_list[i + 1], place, speed)
            block_list.insert(i + 2,
                              blk(False, block_list[i].type, block_list[i + 1] + calc, place, block_list[i + 1].people))
            if dest_bool:
                block_list.insert(i + 3, blk(False, block_list[i].type, block_list[i + 1] + calc + stop, place,
                                             block_list[i + 1].people - 1, True))
            else:
                block_list.insert(i + 3, blk(False, block_list[i].type, block_list[i + 1] + calc + stop, place,
                                             block_list[i + 1].people))
            block_list.insert(i + 4, blk(False, 0, block_list[i + 1] + calc, place, block_list[i + 1].people))
            update_list(i + 4, block_list, stop, speed)
            return i + 4

    return 0


def update_list(place, block_list, time, speed):  # not including place
    for i in range(place, len(block_list)):
        if block_list[i].call_time:
            call_time = block_list.pop(i)
            call_place = add_call_time(call_time.time, block_list, speed)
            add_people(call_place, i, block_list)
        else:
            block_list[i].time += time


def calc_type(place_before, place_now):
    tp = 0
    if place_before < place_now:
        tp = 1
    if place_before > place_now:
        tp = -1
    return tp


def calc_time(place_before, place_now, speed):
    dist = place_before - place_now
    if (dist < 0):
        dist = place_now - place_before
    return dist / speed


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
            add(call, list_copy, self.building.getElevetor(elev))
            total_time = total_time_calculator(list_copy)
            temporary_total_time_List.append(total_time - self.total_time_list[elev])
        minimum = temporary_total_time_List[0]  # Calculate which is the best choose
        ans = 0
        for i in range(len(temporary_total_time_List)):
            if minimum > temporary_total_time_List[i]:
                minimum = temporary_total_time_List[i]
                ans = i
        self.total_time_list[ans] += minimum  # Update the new choose
        self.update_total_time(minimum)
        add(call, self.total_List[ans], self.building.getElevetor(ans))
        return ans
