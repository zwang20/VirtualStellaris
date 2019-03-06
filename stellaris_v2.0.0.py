import random

print('Hello')

object_types = ['Star', 'Planet', 'Astroids', 'Gas Giant']

# Classes
class StarSystem:

    def __init__(self):

        self.objects = [StarSystemObjectSun()]

        for x in range(7):
            if random.randint(0, 1) == 0:
                self.objects.append(StarSystemObjectPlanet())
            else:
                self.objects.append(StarSystemObjectNothing())

    def view(self):
        for x in self.objects:
            x.view()


class StarSystemObject:

    upkeep_points = 0
    production_points = 0

    def __init__(self):
        pass

    def view(self):
        print('upkeep_points,', self.upkeep_points, 'production_points,', self.production_points)


class StarSystemObjectSun(StarSystemObject):

    upkeep_points = 1
    production_points = 0

    def __init__(self):
        super().__init__()


class StarSystemObjectPlanet(StarSystemObject):

    upkeep_points = 0
    production_points = 1

    def __init__(self):
        super().__init__()


class StarSystemObjectNothing(StarSystemObject):

    upkeep_points = 0
    production_points = 0

# Functions
pass

# Game
def main():
    sys1 = StarSystem()
    sys1.view()

# execute game
main()
