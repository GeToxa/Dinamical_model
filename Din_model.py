from Create_Base import creat_traffic, creat_coordinate_scans


xo_ik = 0 # Систояние ИВО в начальынй момент времени
Uo_ikj = 0 # Управляющее воздействие 1 операция выполняется, 0 нет (изначально 0, не выполняется)

class equation_of_din_mess():
    def get_time(self):
