class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc

class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self._max_health = 3
        self.health = 3
        self._desc = " A skinny and foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >=3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

class Barbarian(GameObject):
    def __init__(self, name):
        self.class_name = "barbarian"
        self._max_health = 5
        self.health = 5
        self._desc = " A strong but brainless creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 5:
            return self._desc
        elif self.health == 4:
            health_line = "It has a wound on its knee."
        elif self.health == 3:
            health_line = "It has wounds on its knee and arm."
        elif self.health == 2:
            health_line = "Its left arm has been cut off!"
        elif self.health == 1:
            health_line = "It has wounds all over his body!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


def get_input():
    command = input("☞  ").split()
    if not command: #if nothing provided
        print("You are too shy to say a word.")
        return
    verb_word = command[0]
    if verb_word in special_verb: #shut the program
        return verb_word.upper()
    if verb_word in verb_dict: #assign verb function
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}". format(verb_word))
        return
    if verb_word == "say": #run function
        noun_words = command[1:]
        print(verb(noun_words))
    elif len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))

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
        return "There is no {} here.".format(noun)

def say(noun):
    return 'You said "{}".'.format(" ".join(noun))

def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "You hit the {}".format(thing.class_name)
        if type(thing) == Barbarian:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "You killed the barbarian!"
            else:
                msg = "You hit the {}".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg

def knife(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health = thing.health - 2
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "You knifed the {}".format(thing.class_name)
        if type(thing) == Barbarian:
            thing.health = thing.health - 2
            if thing.health <= 0:
                msg = "You killed the barbarian!"
            else:
                msg = "You knifed the {}".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg

def heal(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if thing.health <= 0:
            msg = "{} is already dead.".format(noun.title())
        elif thing.health == thing._max_health:
            msg = "{} is with full health.".format(noun.title())
        else:
            thing.health += 1
            msg = "You healed {}.".format(noun)
    else:
        msg = "There is no {} here.".format(noun)
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
        msg = "There is no {} here.".format(noun)
    return msg

special_verb = ["leave", "restart"]

verb_dict = {
    "help" : help,
    "say" : say,
    "examine" : examine,
    "hit" : hit,
    "knife" : knife,
    "heal" : heal,
    "revive" : revive,
}

verb_defi = {
    "all" : ", ".join(verb_dict) + ", " + ", ".join(special_verb),
    "help" : "Provide information of specific werbs",
    "say" : "Speak out the verb loud",
    "examine" : "Examine the condition of a specific creature",
    "hit" : "Hit a creature with your fist",
    "knife" : "Strike a creature with a knife",
    "heal" : "Heal a creature a little bit using magic",
    "revive" : "Let a creature reborn",
    "pet" : "To obtain a creature as pet",
    "order" : "Order your pet to attack another creature",
    "leave" : "Wave goodbey to these little creatures",
    "restart" : "Go back through time and to the beginning of the game"
}

#main
goblin = Goblin("Gobbly")
barbarian = Barbarian("Boby")

while True:
    try:
        pyin = get_input()
        if pyin == "LEAVE":
            print("These little creatures will miss you!")
            break
        elif pyin == "RESTART": #restart the whole game
            goblin = Goblin("Gobbly")
            barbarian = Barbarian("Boby")
            print("You went back through time!")
    except KeyboardInterrupt:
        print("\nPlease do not leave without saying!")
