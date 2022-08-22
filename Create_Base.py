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
    for _ in range(3):
        scan_coord = coordinate_scans(random.randint(1, 2), random.randint(1, 3))
        Coordinate_scans_list.append(scan_coord)
    for scans in Coordinate_scans_list:
        print(scans.scantime, scans.KWT)

creat_coordinate_scans()

