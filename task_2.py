class Aircraft:

    def __init__(self, name, max_load, max_capacity):

        self.name = name
        self.max_load = max_load
        self.max_capacity = max_capacity
        self.actual_load = []
        self.actual_capacity = []

    def addBox(self, box_weight, box_size):

        weight = box_weight
        size = box_size

        if weight + sum(self.actual_load) <= self.max_load:

            if size + sum(self.actual_capacity) <= self.max_capacity:

                self.actual_load.append(weight)
                self.actual_capacity.append(size)

                print("\n  Box successfully ADDED! ")
                print("===================================================")
                print("|  Actual number of boxes in {}: {}". format(self.name, len(self.actual_load)))
                print("|  Actual load of {}: {}". format(self.name, sum(self.actual_load)))
                print("===================================================")
                print("|  Weight of boxes in {}: {}".format(self.name, self.actual_load))
                print("===================================================")
                print("|  Size of boxes in {}: {}".format(self.name, self.actual_capacity))
                print("===================================================\n")
            
            else:
                print("\n=========================================================")
                print("               Box can NOT be added!")
                print("---------------------------------------------------------")
                print(" -  Box weight is acceptable, but box size is too big")
                print("=========================================================\n")

        else:
            print("\n=========================================================")
            print("               Box can NOT be added!")
            print("---------------------------------------------------------")
            print(" -  Box is too heavy")
            print("=========================================================\n")

    


class Box:

    def __init__(self, weight, size):

        self.weight = weight
        self.size = size


if __name__ == "__main__":

    aircraft_1 = Aircraft("TurBox01", 15, 120)
    box_1 = Box(2, 14)
    box_2 = Box(3, 8)
    box_3 = Box(8, 50)
    box_4 = Box(1, 60)
    box_5 = Box(4, 40)

    Aircraft.addBox(aircraft_1, box_1.weight, box_1.size)
    Aircraft.addBox(aircraft_1, box_2.weight, box_2.size)
    Aircraft.addBox(aircraft_1, box_3.weight, box_3.size)
    Aircraft.addBox(aircraft_1, box_4.weight, box_4.size)
    Aircraft.addBox(aircraft_1, box_5.weight, box_5.size)


