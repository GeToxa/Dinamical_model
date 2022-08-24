import random
Trafic_list = []
class Some_Loads():
    def __init__(self, Mass, Speed):
        self.Mass = Mass
        self.Speed = Speed
        self.point = 0
        self.end_point = 200
        self.way = self.end_point - self.point
        self.start_time = random.randint(0, 600)

    def get_mass_speed(self):
        self.Mass = round(self.Mass + random.triangular(-2, 2, 0.1))
        self.Speed = round(((self.Speed + random.triangular(-10, 10, 0.1))*360)/1000)
        print(self.Mass, self.Speed)

    def Culc_time(self):
        way_time = self.way / self.Speed
        return way_time
    def get_start(self):
        print(self.start_time)
        return self.start_time
    def get_end_time(self):
        end_time = self.start_time + Some_Loads.Culc_time(self)
        return end_time


class coordinate_scans():
    def __init__(self, scantime, coordinate_work, KWT):
        self.scantime = scantime
        self.KWT = KWT
        self.basic_period = 1
        self.range_of_work = 50
        self.coordinate_work = coordinate_work
        self.coordinate_of_range_start = self.coordinate_work - 25
        self.coordinate_of_range_end = self.coordinate_work + 25

