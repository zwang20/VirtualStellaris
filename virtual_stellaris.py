import random

# class Planet:
#     objects = []
#
#     def __init__(self, name, pp, up):
#         self.name = name
#         self.pp = pp
#         self.up = up
#         Planet.objects.append(self)

ship_names = open('ShipNames.txt', 'r').read().split('\n')
fleet_names = open('FleetNames.txt', 'r').read().split('\n')
system_names = open('SystemNames.txt', 'r').read().split('\n')

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
        temp_name = random.choice(system_names)
        while temp_name in System.object_names:
            temp_name = random.choice(system_names)
        print('System', temp_name, 'was created')
        self.name = temp_name
        del temp_name
        self.planets = [random.choice(planet_type_list) for i in range(8)]

        System.objects.append(self)

        System.renew()

    def renew():
        temp_list = []
        for i in System.objects:
            temp_list.append(i.name)
        System.object_names = temp_list
        del temp_list

    def modify_name(self, name):
        if name not in System.object_names():
            self.name = name
        System.renew()

    def modify_discription(self, description):
        self.discription = discription
        System.renew()

    def get_info(self):
        return self.planets

class Fleet:
    objects = []
    object_names = []

    def __init__(self, alligence):
        temp_name = random.choice(fleet_names)
        while temp_name in Fleet.object_names:
            temp_name = random.choice(fleet_names)
        print('Fleet', temp_name, 'was created')
        self.name = temp_name
        del temp_name
        self.alligence = alligence

        Fleet.objects.append(self)

        Fleet.renew()

    def renew():
        temp_list = []
        for i in Fleet.objects:
            temp_list.append(i.name)
        Fleet.object_names = temp_list
        del temp_list

class Ship:
    objects = []
    object_names = []

    def __init__(self, alligence):
        temp_name = random.choice(ship_names)
        while temp_name in Ship.object_names:
            temp_name = random.choice(ship_names)
        print('Ship', temp_name, 'was created')
        self.name = temp_name
        del temp_name
        self.alligence = alligence

        Ship.objects.append(self)

        Ship.renew()

    def renew():
        temp_list = []
        for i in Ship.objects:
            temp_list.append(i.name)
        Ship.object_names = temp_list
        del temp_list

    def get_info(self):
        return 'alligence' + self.alligence

def info_ship(noun):
    if noun in Ship.object_names:
        return Ship.objects[Ship.object_names.index(noun)].get_info()


def info_system(noun):
    if noun in System.object_names:
        return System.objects[System.object_names.index(noun)].get_info()

def game():
    while True:
        pass
