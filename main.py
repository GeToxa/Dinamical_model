import random

class Some_Loads():
    def __init__(self, Mass, Speed):
        self.Mass = Mass
        self.Speed = Speed
        self.point = 0
        self.end_point = 200
        self.way = self.end_point - self.point

    def get_mass_speed(self):
        self.Mass = round(self.Mass + random.triangular(-2, 2, 0.1))
        self.Speed = round(self.Speed + random.triangular(-10, 10, 0.1))
        print(self.Mass, self.Speed)

    def Culc_time(self):
        way_time = self.way / self.Speed
        return way_time


Trafic_list = []


def creaete_tr_load():

    for i in range(7):
        Traffic_load = Some_Loads(5, 80)
        Traffic_load.get_mass_speed()
        Trafic_list.append(Traffic_load)

creaete_tr_load()

