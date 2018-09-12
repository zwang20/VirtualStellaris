from os import system
from time import time
from random import randint

BLOCK = 0.3

class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc

class Character(GameObject):
    def __init__(self, name, desc):
        self.class_name = "explorer"
        self._max_health = 80
        self.health = 80
        self._desc = ' ' + desc
        GameObject.pet = None
        GameObject.explorer = self
        super().__init__(name)

    @property
    def desc(self):
        if self.health == 80:
            return self._desc
        elif self.health > 60:
            health_line = "You are slightly wounded."
        elif self.health > 40:
            health_line = "Your arms and legs have been badly hurt."
        elif self.health > 20:
            health_line = "You are suffering extreme pain!"
        elif self.health > 0:
            health_line = "You are dying."
        else:
            health_line = "You are dead!"
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

class Goblin(GameObject):
    family = []
    def __init__(self, name):
        self.class_name = "goblin"
        self._max_health = 25
        self.health = 25
        self.attack = (7,12)
        self._desc = " A skinny and foul creature"
        self._attack_desc = "Goblin stike you at an lightening speed."
        super().__init__(name)

    @property
    def desc(self):
        if self.health == 25:
            return self._desc
        elif self.health > 18:
            health_line = "It has a wound on its knee."
        elif self.health > 9:
            health_line = "Its left arm has been cut off!"
        elif self.health > 0:
            health_line = "Its arms has been cut off!"
        else:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

class Barbarian(GameObject):
    family = []
    def __init__(self, name):
        self.class_name = "barbarian"
        self._max_health = 50
        self.health = 50
        self.attack = (9,10)
        self._desc = " A strong but brainless creature"
        self._attack_desc = "Barbarian hit you with his heavy sword."
        super().__init__(name)

    @property
    def desc(self):
        if self.health == 50:
            return self._desc
        elif self.health > 40:
            health_line = "It has a wound on its knee."
        elif self.health > 30:
            health_line = "It has wounds on its knee and arm."
        elif self.health > 20:
            health_line = "Its left arm has been cut off."
        elif self.health > 10:
            health_line = "It has wounds all over his body!"
        elif self.health > 0:
            health_line = "It is dying!"
        else:
            health_line = "It is dead."
        return self._desc + "\n" + health_line
        explorer.health -= randint(*thing.attack)

    @desc.setter
    def desc(self, value):
        self._desc = value

class Giant(GameObject):
    family = []
    def __init__(self, name):
        self.class_name = "giant"
        self._max_health = 100
        self.health = 50
        self.attack = (2, 3)
        self._desc = " An extreme strong and friendly creature"
        self._attack_desc = "The giant just don not want to harm anyone."
        super().__init__(name)

    @property
    def desc(self):
        if self.health == 100:
            return self._desc
        elif self.health > 80:
            health_line = "It has wounds on his left arm."
        elif self.health > 60:
            health_line = "It has long cuts on his body."
        elif self.health > 40:
            health_line = "It is bleeding"
        elif self.health > 20:
            health_line = "It is screaming loudly because of huge pain."
        elif self.health > 0:
            health_line = "It looks extremely tired and suffering."
        else:
            health_line = "It is dead."
        return self._desc + "\n" + health_line
        explorer.health -= randint(*thing.attack)

    @desc.setter
    def desc(self, value):
        self._desc = value

def get_input():
    command = input("💬  ").split()
    if not command: #if nothing provided
        print("You are too shy to say a word.")
        return
    verb_word = command[0]
    if verb_word in passive_verb:
        print("Passive verbs can only be triggered under some circumstances!")
        return
    #game-wide operation
    if verb_word in special_verb:
        return verb_word.upper()
    #assign verb function
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}". format(verb_word))
        return
    #run function
    if verb_word == "say":
        noun_words = command[1:]
    elif verb_word == "create":
        noun_words = command[1:3]
    elif len(command) >= 2:
        noun_words = command[1]
    else:
        noun_words = "nothing"
    print(verb(noun_words))
    return "ValidCycle"

def block(attacker):
    print('🛡  {} fought back, type in "block" to block'.format(attacker))
    start = time()
    string = input()
    end = time()
    if string != "block":
        return (0, "You failed to block the attack.")
    else:
        ratio = (1 / BLOCK - end + start) * BLOCK
        if ratio >= 1.00:
            return (1, "You avoided the attack")
        elif ratio >= 0.75:
            return (ratio, "You nearly get away with it.")
        elif ratio >= 0.50:
            return (ratio, "Your defense made a difference.")
        elif ratio >= 0.25:
            return (ratio, "Your defense was not effective.")
        else:
            return (0, "You did not manage to block the attack.")

def get(noun):
    return ", ".join(GameObject.objects)

def help(noun):
    if noun in verb_defi:
        msg = "{}\n {}".format(noun,verb_defi[noun])
    elif noun == "nothing":
        msg = verb_defi["all"]
    else:
        msg = "There is no information about {}.".format(noun)
    return msg

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here!".format(noun)

def say(noun):
    if noun:
        return 'You said "{}"'.format(" ".join(noun))
    else:
        return 'You said nothing.'

def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Character:
            return "You can not hit yourself!"
        elif thing.health <= 0:
            return "You have already killed {}.".format(thing.class_name)
        elif GameObject.pet == thing:
            return "You can not harm your pet!"
        bonus = randint(-1,1)
        thing.health = thing.health - 8 + bonus
        if bonus == -1:
            msg = "You hit {} in its stomach.".format(thing.class_name)
        elif bonus == 0:
            msg = "You hit {} in its chest.".format(thing.class_name)
        elif bonus == 1:
            msg = "You hit {} right in its head!".format(thing.class_name)
        if thing.health <= 0:
            msg += "\nYou killed the {}!".format(thing.class_name)
        else:
            reduc, block_mes = block(thing.class_name)
            GameObject.explorer.health -= randint(*thing.attack) * (1 - reduc)
            msg += '\n' +  thing._attack_desc + '\n' + block_mes
    else:
        msg = "There is no {} here!".format(noun)
    return msg

def knife(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Character:
            return "You can not knife yourself!"
        elif thing.health <= 0:
            return "You have already killed {}.".format(thing.class_name)
        elif GameObject.pet == thing:
            return "You can not harm your pet!"
        bonus = randint(-3,3)
        thing.health = thing.health - 20 + bonus
        if bonus <= -2:
            msg = "You knifed the {}'s arm".format(thing.class_name)
        elif bonus <= 1:
            msg = "You knifed the {}'s stomach.".format(thing.class_name)
        else:
            msg = "You knifed the {} with a combo.".format(thing.class_name)
        if thing.health <= 0:
            msg += "\nYou killed the {}!".format(thing.class_name)
        else:
            reduc, block_mes = block(thing.class_name)
            GameObject.explorer.health -= randint(*thing.attack) * (1 - reduc)
            msg += '\n' +  thing._attack_desc + '\n' + block_mes
    else:
        msg = "There is no {} here!".format(noun)
    return msg

def heal(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if thing.health <= 0:
            msg = "{} is already dead.".format(noun.title())
        elif thing.health == thing._max_health:
            msg = "{} is with full health.".format(noun.title())
        else:
            thing.health += 10
            if thing.health > thing._max_health:
                thing.health = thing._max_health
            msg = "You healed {}.".format(noun)
    else:
        msg = "There is no {} here!".format(noun)
    return msg

def revive(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if thing.health > 0:
            msg = "{} is still alive!".format(noun.title())
        else:
            thing.health = thing._max_health
            msg = "You revived {}.".format(noun)
    else:
        msg = "There is no {} here!".format(noun)
    return msg

def pet(noun):
    if not GameObject.pet:
        if noun in GameObject.objects:
            thing = GameObject.objects[noun]
            if thing == GameObject.explorer:
                return "You can not pet yourself!"
            if thing.health <= 0:
                return "{} is already dead!".format(noun.title())
            GameObject.pet = thing
            return "{} has now become your pet.".format(noun.title())
        else:
            return "There is no {} here!".format(noun)
    else:
        return "You have already obtained a pet!"

def cast(noun):
    if GameObject.pet != None:
        pet_name = GameObject.pet.class_name
        GameObject.pet = None
        return "You have abandoned {}.".format(pet_name)
    else:
        return "You have not got a pet yet!"

def order(noun):
    if GameObject.pet == None:
        return "You have not got a pet yet!"
    elif noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Character:
            return "You can not hit yourself!"
        elif thing.health <= 0:
            return "You have already killed {}.".format(thing.class_name)
        elif GameObject.pet == thing:
            return "You can not order your pet to attack itself!"
        pet_attack = randint(*GameObject.pet.attack)
        thing.health -= pet_attack
        msg = GameObject.pet._attack_desc.replace("you", noun)
        if thing.health <= 0:
            msg += "\nYou killed the {}!".format(thing.class_name)
        else:
            GameObject.pet.health -= randint(*thing.attack)
            msg += '\n' + thing._attack_desc.replace("you", "your pet")
            if GameObject.pet.health <= 0:
                GameObject.pet = None
                msg += '\n' + "Your pet is dead"
        return msg
    else:
        return "There is no {} here!".format(noun)

def create(nouns):
    if len(nouns) < 1:
        return "You nedd to specify a species!"
    elif len(nouns) < 2:
        return "You nedd to specify a name!"
    species = nouns[0]
    name = nouns[1]
    if name in GameObject.objects:
        return "Creature with the name {} already exist!".format(name)
    if species == "goblin":
        Goblin.family.append(Goblin(name))
    elif species == "barbarian":
        Barbarian.family.append(Barbarian(name))
    elif species == "giant":
        Giant.family.append(Giant(name))
    else:
        return "Unknown species {}!".format(species)
    return "A {} named {} is created.".format(species,name)

def vanish(noun):
    if noun == GameObject.explorer.name:
        return "You can not vanish yourself!"
    elif noun in GameObject.objects:
        thing = GameObject.objects[noun]
        type(thing).family.remove(thing)
        del GameObject.objects[noun]
        return "You removed {} from the game.".format(noun)
    else:
        return "There is no {} here!".format(noun)

passive_verb = ("block")

special_verb = ("leave", "restart")

verb_dict = {
    "get" : get,
    "help" : help,
    "say" : say,
    "examine" : examine,
    "hit" : hit,
    "knife" : knife,
    "heal" : heal,
    "revive" : revive,
    "pet" : pet,
    "cast" : cast,
    "order" : order,
    "create" : create,
    "vanish" : vanish,
}

verb_defi = {
    "all" : ", ".join(verb_dict) + ", " + ", ".join(special_verb),
    "get" : "[game] Get all the characters that are currently in the game",
    "help" : "[game] Provide information of a specific verb",
    "say" : "[action] Speak out the verb loud",
    "examine" : "[action] Examine the condition of a specific creature",
    "hit" : "[action] Hit a creature with your fist",
    "knife" : "[action] Strike a creature with a knife",
    "heal" : "[action] Heal a creature a little bit using magic",
    "revive" : "[action] Let a creature reborn",
    "pet" : "[action] To obtain a creature as pet",
    "cast" : "[action] To abandon the creature you keep as pet",
    "order" : "[action] Order your pet to attack another creature",
    "create" : "[game] Create a new creature by specifying its race and name",
    "vanish" : "[game] To make a creature completely disappear",
    "block" : "[passive] To block an attack from other wild creatures",
    "leave" : "[game] Wave goodbey to these little creatures",
    "restart" : "[game] Go back to the beginning of the game",
}

#main
def main():
    GameObject.objects.clear()
    Goblin.family = [Goblin("Gobbly")]
    Barbarian.family = [Barbarian("Boby")]
    Giant.family = [Giant("Mightie")]
    print("What is your name, great explorer?")
    nickname = input("💬  ")
    while len(nickname) >= 12 or not nickname or ' ' in nickname:
        print("Your nickname can not contain space or more than 12 characters.")
        print("What is your name, great explorer?")
        nickname = input("💬  ")
    print("What is your motto, {}?".format(nickname))
    motto = input("💬  ")
    while len(motto) >= 30 or not motto:
        print("Your motto should be at most 30 characters!")
        print("What is your motto, {}?".format(nickname))
        motto = input("💬  ")
    explorer = Character(nickname,motto)

if __name__ == "__main__":
    system("clear")
    try:
        main()
    except KeyboardInterrupt:
        print("\nHope we will see you again soon!")
        exit()

    while True:
        try:
            pyin = get_input()
            if pyin == "LEAVE":
                print("These little creatures will miss you!")
                break
            elif pyin == "RESTART": #restart the whole game
                print("You have gone back to the beginning of the game!")
                system("clear")
                main()
            elif GameObject.explorer.health <= 0:
                system("clear")
                print("You are dead! Game has been reset.")
                main()
        except KeyboardInterrupt:
            print("\nPlease do not leave without saying!")
