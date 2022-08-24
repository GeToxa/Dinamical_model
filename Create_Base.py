from Classes import Some_Loads, coordinate_scans
import random
#Для проверки работы репозиритория

Coordinate_scans_list = []
Traffic_list = []

def creat_traffic():
    for _ in range(3):
        Traffic = Some_Loads(5, 80)
        Traffic.get_mass_speed()
        Traffic_list.append(Traffic)

    for Traffics in Traffic_list:
        Traffics.get_start()
        Traffics.get_end_time()

creat_traffic()

def creat_coordinate_scans():
    place = 0
    for _ in range(3):
        scan_coord = coordinate_scans(random.randint(1, 2), place + 100, random.randint(1, 3))
        Coordinate_scans_list.append(scan_coord)
        place += 100
    for scans in Coordinate_scans_list:
        print(scans.scantime, scans.coordinate_work, scans.KWT)

creat_coordinate_scans()

def get_cross():
    Traffic_way_time_list = []
    for Traffics in Traffic_list:
        way_time = Traffics.get_end_time()
        Traffic_way_time_list.append(way_time)
    max_way_time = max(Traffic_way_time_list)
    min_way_time = min(Traffic_way_time_list)
    print(max_way_time, min_way_time)



get_cross()


