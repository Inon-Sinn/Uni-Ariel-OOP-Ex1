import json
import csv
from Classes import Building as bld
from Classes import Elevator as elv
from Classes import CallforElevator as call


def load_json_building(file_name) -> bld.Building:
    try:
        with open(file_name, "r+") as f:
            my_d = json.load(f)
            elevList = list()
            for v in my_d['_elevators']:
                elev = elv.Elevator(id=v["_id"], speed=v["_speed"], minFloor=v["_minFloor"], maxFloor=v["_maxFloor"],
                                    closeTime=v["_closeTime"], openTime=v["_openTime"], startTime=v["_startTime"],
                                    stopTime=v["_stopTime"])
                elevList.append(elev)
            return bld.Building(my_d["_minFloor"], my_d["_maxFloor"], elevList)
    except IOError as err:
        print(err)


# def load_json_elevator(self, file_name):
#     try:
#         with open(file_name, "r+") as f:
#             my_d = json.load(f)
#             e = elv.Elevator(my_d["_id"], my_d["_speed"], my_d["_minFloor"], my_d["_maxFloor"],
#                              my_d["_closeTime"], my_d["_openTime"], my_d["_startTime"], my_d["_stopTime"])
#     except IOError as err:
#         print(err)


def load_csv_call(file_name):
    calls = []
    with open(file_name) as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            c = call.CallforElevator(time=row[1], src=row[2], dest=row[3], state=row[4], allocated_to=row[5])
            calls.append(c)
    return calls


def call_to_csv(call_list, file_name):
    rows = []
    for c in call_list:
        rows.append(["Elevator call", c.time, c.src, c.dest, c.state, c.allocated_to])
    with open(file_name, 'w', newline="") as f:
        cswriter = csv.writer(f)
        cswriter.writerows(rows)


if __name__ == '__main__':
    path_Json = "Ex1_input/Ex1_Buildings/B1.json"
    path_csv = "Ex1_input/Ex1_Calls/Calls_a.csv"

    MyBuilding = load_json_building(path_Json)
    # print(MyBuilding)
    # num = MyBuilding.getNumofElevators()
    # for i in range(MyBuilding.getNumofElevators()):
    #     print(MyBuilding.getElevetor(i),"\n")

    MyCsv = load_csv_call(path_csv)
    # print(MyCsv)
    call_to_csv(MyCsv, 'newCsv2.csv')
