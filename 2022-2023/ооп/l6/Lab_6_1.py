class Building:
    def __init__(self, stage_counter):
        self.stage_counter = stage_counter
        self.stages = ['']*stage_counter
    

    def __setitem__(self, stage_number, stage_name):
        if not isinstance(stage_number, int):
            raise TypeError("Индекс должен быть целым числом")
        if stage_number >= self.stage_counter or stage_number < 0:
            raise TypeError("Недопустимый этаж")

        # self.stages.insert(stage_number-1, stage_name)
        self.stages[stage_number] = stage_name


    def __getitem__(self, stage_number):
        if not isinstance(stage_number, int):
            raise TypeError("Индекс должен быть целым числом")
        if stage_number >= self.stage_counter or stage_number < 0:
            raise TypeError("Недопустимый этаж")
        
        if self.stages[stage_number]:
            return(self.stages[stage_number])
        else:
            return None


    def __delitem__(self, stage_number):
        if not isinstance(stage_number, int):
            raise TypeError("Индекс должен быть целым числом")
        if stage_number >= self.stage_counter or stage_number < 0:
            raise TypeError("Недопустимый этаж")

        self.stages[stage_number] = ''
        print(f'{stage_number} was deleted')
            

iron_building = Building(12)  # Создаем здание с 12 этажами 
iron_building[0] = 'Morgan Stanley' 
iron_building[2] = 'IBM' 
iron_building[4] = 'Boeing' 
iron_building[6] = 'Amazon.com' 
iron_building[11] = ' Intel' 

del iron_building[4]

for i in range(0, iron_building.stage_counter):
    print(f"{i} - {iron_building[i]}")