import Classes
import Block as blk


def add_block(new_block: blk, block_list: list):
    if(len(block_list)==0):
        block_list.append(new_block)
    else:
        for i in range(len(block_list)-1):#check for all except the last
            if ((block_list[i].call_time + block_list[i].total_time) <= new_block.call_time) & ((block_list[i + 1].call_time + block_list[i + 1].total_time) <= (new_block.call_time + new_block.total_time)):
                new_block.update(block_list[i].dest)

            if()



class Allocation:

    def __init__(self, building, call_list):
        self.building = building
        self.call_list = call_list
        self.total_time = 0  # helper
        self.total_List = list()
        self.allocation = list()
        self.total_time_list = list()

        for i in range(building.getNumofElevators()):  # check if its working
            self.total_List.append([])

        for i in range(building.getNumofElevators()):  # check if its working
            self.total_time_list.append(0)

        for c in call_list:
            self.allocation.append(self.allocate_call(c))

    def update_total_time(self, time):
        self.total_time += time

    def allocate_call(self, call):
        tempory_total_time_List = list()
        block = blk.Block(1, 2, 5, 4, 9)
        for elev in range(len(self.total_List)):  # goes to over the elvetors for the calculation
            list_copy = self.total_List[elev].copy()
            self.addBlock(block, list_copy)
            total_time = 0
            for block in list_copy:
                total_time += block.total_time
            tempory_total_time_List.append(total_time - self.total_time_list[elev])

        min = tempory_total_time_List[0]  # Calculate which is the best choose
        ans = 0
        for i in range(len(tempory_total_time_List)):
            if min > tempory_total_time_List[i]:
                min = tempory_total_time_List[i]
                ans = i

        self.total_time_list[ans] += min  # Update the new choose
        self.update_total_time(tempory_total_time_List[ans])
        self.addBlock(block, self.total_List[i])
        return ans
