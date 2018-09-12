print ('Hello')
Help = ('Commands are used to interact with the game\n\
A list of commands include:\n\
ViewSystem - This is used to view each system\n\
ViewFleet - This is used to view your fleets\n\
Map - This is used to see a crude map of the galaxy\n\
Quit - This is used to end the program\n\
EndTurn - This is used to end the turn\n\
These commands are case sensitive')
print(Help)
SystemA = ('System Information\n\
Disctiption:\n\
This system is the defult start system\n\
It connects to system b\n\
Star     1UP\n\
Planet   1PP\n\
Planet   1PP\n\
Planet   1PP\n\
Astroids 3PP\n\
GasGiant 1UP')
SystemB = ('System Information\n\
Disctiption:\n\
This system is the only system connected to system a\n\
It connects to system a,e, and f\n\
Star     1UP\n\
Planet   1PP\n\
Planet   1PP\n\
GasGiant 1UP\n\
GasGiant 1UP')
SystemE = ('System Information\n\
Disctiption:\n\
This system is a bonus system\n\
It connects to system b and f\n\
Star     1UP\n\
Astroids 3PP\n\
Astroids 3PP\n\
Astroids 3PP')
SystemF = ('System Information\n\
Disctiption:\n\
This system is the only system connected to system g\n\
It connects to system b, e, and g\n\
Star     1UP\n\
Planet   1PP\n\
Planet   1PP\n\
GasGiant 1UP\n\
GasGiant 1UP')
SystemG = ('System Information\n\
Disctiption:\n\
This system is the defult start system for the enemy\n\
It connects to system f\n\
Star     1UP\n\
Planet   1PP\n\
Planet   1PP\n\
Planet   1PP\n\
Astroids 3PP\n\
GasGiant 1UP')
SystemAOwner = 'Player'
SystemBOwner = 'Neutral'
SystemEOwner = 'Neutral'
SystemFOwner = 'Neutral'
SystemGOwner = 'Enemy'
PlayerFleet1 = ['SciShip1']
PlayerFleet2 = ['ConShip1']
PlayerFleet3 = ['WarShip1','WarShip2']
PlayerFleet4 = []
EnemyFleet1 = []
EnemyFleet2 = []
EnemyFleet3 = []
EnemyFleet4 = []
ProductionPoints = 5
UpkeepPoints = 5
while True:
    ActionPoints = 15
    while ActionPoints > 0:
        MainCommand = input ('Input Command: ')
        if MainCommand == 'ViewSystem':
            System = input ('Input System: ')
            if System == 'A':
                print('System A')
                print(SystemA)
            elif System == 'B':
                print('System B')
                print(SystemB)
            elif System == 'E':
                print('System E')
                print(SystemE)
            elif System == 'F':
                print('System F')
                print(SystemF)
            elif System == 'G':
                print('System G')
                print(SystemG)
            else:
                print('System Not Found')
        elif MainCommand == 'ViewFleet':
            Fleet = input('Input Fleet: ')
            if Fleet == '1':
                print (PlayerFleet1)
            elif Fleet == '2':
                print (PlayerFleet2)
            elif Fleet == '3':
                print(PlayerFleet3)
            elif Fleet == '4':
                print(PlayerFleet4)
            else:
                print ('Fleet not found')
        elif MainCommand == 'Help':
            print(Help)
        elif MainCommand == 'Map':
            print('\n a-b\n   |'+'\ '+'\n   e-f-g\n')
        elif MainCommand == 'Quit':
            raise SystemExit
        elif MainCommand == 'EndTurn':
            ActionPoints = 0
        elif MainCommand == 'Debug':
            Debug = input('Debug Command: ')
            if Debug == 'ActionPointAdd':
                ActionPointAdd = int(input('How much: '))
                ActionPoints = ActionPoints + ActionPointAdd
            elif Debug == 'ActionPointSet':
                ActionPointSet = int(input('How much: '))
                ActionPoints = ActionPointSet
            elif Debug == 'ClearFleets':
                ClearFleets = input('Are you sure?\n\
Doing so will remove all the fleets in existance\n\
(Y/N): ')
                if ClearFleets == 'Y':
                    PlayerFleet1 = []
                    PlayerFleet2 = []
                    PlayerFleet3 = []
                    PlayerFleet4 = []
                    EnemyFleet1 = []
                    EnemyFleet2 = []
                    EnemyFleet3 = []
                    EnemyFleet4 = []
                else:
                    print('No fleets are harmed in the process')
            else:
                print ('Command Not Found')
        else:
            print ("Command Not Found\n\
Use the command 'Help' if you need help")
    print('Turn Ended')
    print('Processing')
    print('Your Turn')

