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
print (planet_type_list)

class System:
    objects = []

    def __init__(self, name, description):
        self.name = name
        self.discription = description
        self.planets = [random.choice(planet_type_list) for i in range(8)]
        print (self.planets)
        System.objects.append(self)

System('Test', 'Blame Edward')
