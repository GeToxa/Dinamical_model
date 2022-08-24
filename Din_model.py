from Create_Base import creat_traffic, creat_coordinate_scans, get_time_bending, Coordinate_scans_list


Scans = Coordinate_scans_list

xo_ik = 0 # Систояние ИВО в начальынй момент времени
Uo_ikj = 0 # Управляющее воздействие 1 операция выполняется, 0 нет (изначально 0, не выполняется)


Time = []
def get_time():
    Bending_of_time = get_time_bending()
    print(Bending_of_time[1], Bending_of_time[0])
    for i in range(Bending_of_time[1], Bending_of_time[0] + 1, 1):
        Time.append(i)
get_time()
print(Time)

class equation_of_din_mess():
    def __init__(self):
        self.Time = Time
    def equation(self):
        for Times in self.Time:
            for i in range(len(Scans)):
                x_o_ik[Times + 1] = x_o_ik[Times] + Eij[i] * U_o_ikj[Times]
