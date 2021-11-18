import json
import csv
from Classes.Building import Building as bld
from Classes.Elevator import Elevator as elv
from Classes.CallforElevator import CallforElevator as call
from Classes.Allocation import Allocation as alc
import sys
import os


def load_json_building(file_name) -> bld:
    try:
        with open(file_name, "r+") as f:
            my_d = json.load(f)
            elevList = list()
            for v in my_d['_elevators']:
                elev = elv(id=v["_id"], speed=v["_speed"], minFloor=v["_minFloor"], maxFloor=v["_maxFloor"],
                           closeTime=v["_closeTime"], openTime=v["_openTime"], startTime=v["_startTime"],
                           stopTime=v["_stopTime"])
                elevList.append(elev)
            return bld(my_d["_minFloor"], my_d["_maxFloor"], elevList)
    except IOError as err:
        print(err)


def load_csv_call(file_name):
    calls = []
    with open(file_name) as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            c = call(time=row[1], src=row[2], dest=row[3], state=row[4], allocated_to=row[5])
            calls.append(c)
    return calls


def call_to_csv(call_list, file_name):
    rows = []
    for c in call_list:
        rows.append(["Elevator call", c.time, c.src, c.dest, c.state, c.allocated_to])
    with open(file_name, 'w', newline="") as f:
        cswriter = csv.writer(f)
        cswriter.writerows(rows)


def main():
    path_json = ""
    path_csv = ""
    if len(sys.argv) <= 1:
        # scenario settings
        while True:
            try:
                path_json = input("json path for building and elevators: ")
                break
            except:
                print("Wrong file type/path!  Try again.\n")
                continue

        while True:
            try:
                path_csv = input("csv path for calls: ")
                break
            except:
                print("Wrong file type/path!  Try again.\n")
                continue
    else:
        path_json = sys.argv[1]
        path_csv = sys.argv[2]
    # check if files exist
    building_exist = os.path.isfile(path_json)
    calls_exist = os.path.isfile(path_csv)
    if not building_exist:
        path_json = "Ex1_input\\Ex1_Buildings\\" + path_json
    if not calls_exist:
        path_csv = "Ex1_input\\Ex1_Calls\\" + path_csv

    MyBuilding = load_json_building(path_json)
    MyCsv = load_csv_call(path_csv)
    aloc = alc(MyBuilding, MyCsv)

    # each call in the list_of_calls is allocated to an elev now, extract this data to a new csv file!
    new_file_name = "output/csv/Result_B1_b.csv"
    for c in range(len(MyCsv)):
        MyCsv[c].allocated_to = aloc.allocation[c]

    if len(sys.argv) <= 1:
        call_to_csv(MyCsv, new_file_name)
        print(new_file_name, "created, run completed successfully.")
    else:
        call_to_csv(MyCsv, sys.argv[3])
        print(sys.argv[3], "created, run completed successfully.")


if __name__ == '__main__':
    main()
    # path_Jso = "Ex1_input/Ex1_Buildings/B1.json"
    # # path_cs = "Ex1_input/Ex1_Calls/Calls_a.csv"
    # path = "Ex1_input/Ex1_Calls/Calls_c.csv"
    #
    # MyBuilding = load_json_building(path_Jso)
    # MyCsv = load_csv_call(path)
    #
    # aloc = alc(MyBuilding, MyCsv)
    # for c in range(len(MyCsv)):
    #     MyCsv[c].allocated_to = aloc.allocation[c]
    #
    # call_to_csv(MyCsv, 'output/csv/Allocation_Test_1.csv')
