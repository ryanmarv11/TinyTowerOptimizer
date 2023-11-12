class Citizen:
    def __init__(self, skillString, dreamJob):
        self.skillString = skillString
        self.dreamJob = dreamJob
        self.creative = int(self.skillString[0])
        self.retail = int(self.skillString[1])
        self.food = int(self.skillString[2])
        self.service = int(self.skillString[3])
        self.recreation = int(self.skillString[4])
        self.job = None
        self.inDreamJob = False

    def assignJob(self, floor):
        self.job = floor.name
        if self.job == self.dreamJob:
                self.inDreamJob = True


class Floor:
    def __init__(self, name):
        self.name = name
        self.employees = []



print("Something")
print("Hello, world! This is my Tiny Tower Optimizer...or at least it will be.")
