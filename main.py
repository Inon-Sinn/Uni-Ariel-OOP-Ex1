import json
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


# def load_csv_call(self, file_name):
#     try:
#         with open(file_name, "r+") as f:
#             my_d = json.load(f)
#             c = call.CallforElevator(my_d["_state"], my_d["_time"], my_d["_src"], my_d["_dest"],
#                                      my_d["_type"], my_d["_allocated_to"])
#     except IOError as err:
#         print(err)

if __name__ == '__main__':
    path = "Ex1_input/Ex1_Buildings/B1.json"
    MyBuilding = load_json_building(path)
    print(MyBuilding)
    num = MyBuilding.getNumofElevators()
    for i in range(MyBuilding.getNumofElevators()):
        print(MyBuilding.getElevetor(i),"\n")
