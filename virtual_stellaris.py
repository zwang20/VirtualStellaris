
class Planet:
    objects = []

    def __init__(self, name, pp, up):
        self.name = name
        self.pp = pp
        self.up = up
        Planet.objects.append(self)


        
class System:
    objects = []

    def __init__(self, name, description, p1, p2, p3, p4, p5, p6, p7, p8,):
        self.name = name
        self.discription = description
        System.objects.append(self)
