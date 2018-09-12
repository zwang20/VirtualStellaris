import random

# class Planet:
#     objects = []
#
#     def __init__(self, name, pp, up):
#         self.name = name
#         self.pp = pp
#         self.up = up
#         Planet.objects.append(self)

random_names = open('names.txt', 'r').read().split('\n')

planet_dict = {
    '' : [0, 0],
    'planet' : [1, 0],
    'asteroid' : [3, 0],
    'gas_giant' : [0, 1],
}

planet_type_list = [key for key in planet_dict.keys()]

class System:
    objects = []
    object_names = []

    def __init__(self):
        self.discription = ''
        temp_name = random.choice(random_names)
        while temp_name in System.objects:
            temp_name = random.choice(random_names)
        self.name = temp_name
        del temp_name
        self.discription = description
        self.planets = [random.choice(planet_type_list) for i in range(8)]
        print (self.planets)
        System.objects.append(self)

    def renew():
        temp_list = []
        for i in System.objects:
            temp_list.append(i.name)
        object_names = temp_list
        del temp_list

    def modify_name(self, name):
        if name not in System.objects():
            self.name = name

    def modify_discription(self, description):
        self.discription = discription

class PlayerFleet:
    objects = []

    def __init__(self):
        pass

System.renew()
