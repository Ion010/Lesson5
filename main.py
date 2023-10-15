#class human():
   # name = ''
   # age = 0
    #def walk(self):
    #    return "Walk"
  #  def talk(selfself):
    #    return "Talk"
#def person(name, age):
   # human.name = name
   # human.age = age
    #print('Name :', human.name, 'Age:', human.age)

#person('Test1',  123)
#person('Test2',  132412)
#person('Test3',  658)


#class animal:   #un obiect
    #def __init__(self, Name, Type, Age):  #metode
        #self.name = Name * 2  #self este declarat doar in el   self.name
        #self.type = Type
       # self.age = Age

#dog = animal('DogName', 'dog', 2)  #dog este un obiect de tip animal
#cat = animal('Tusic', 'cat', 1)   # cat este un obiect type

#print(dog.name)  #display objectName. VariableName => dog name
#print(dog.type)
#print(dog.age)



#declararea variabelor globale
players = [] #array
heal_power = 15

class characters():
    Name = ''
    Hp = 0
    Armor = 0
    Damage = 0

    def __init__(self, name, hp, armor, damage):
        self.Name = name
        self.Hp = hp
        self.Armor = armor
        self.Damage = damage


class game(characters):
    def heal(self):
        global heal_power
        self.Hp += heal_power   #sau self.Hp = self.Hp + heal_power
        print(self.Name , 'have hp = ', self.Hp, 'left')
    def attack(self, Damage):
        if self.Hp - Damage > 0:
            if self.Armor >= 0: #Hp 100, Damge = 20, Armor = 40
                self.Armor - Damage
                self.Hp = self.Hp - (Damage/2)


            else:
                self.Hp = self.Hp - Damage

            print(self.Name , 'have' , self.Hp , 'left' , self.Armor, 'Armor left')
            return True
        else:
            print(self.Name, 'Died')
            return False
while 1:
    try:
        confirmation = input('Enter any key to start')
        break
    except:
        print('Wrong data input')
        continue

hp =int(input('Enter players hp'))
armor = int(input('Enter players armor'))
damage = int(input('Enter players damage power'))
for i in range(0, 2):
    name = input('Enter player name')
    players.append(game(name, hp, armor, damage))

alive = True #verifica daca toti sunt in viata
player1 = players[0]
player2 = players[1]

current_player = player1
next_player = player2

while alive: #daca alive este True joaca va continuadaca alive este false se va afisa cine a pierdut
    print('Turn to choose for' , current_player.Name )

    print('Enter 1 to attack')
    print('Enter 2 to heal')
    print('Enter 3 to continue')
    move = int(input())


    if move == 1:
        alive = next_player.attack(current_player.Damage)
    elif move == 2:
        current_player.heal()
    elif move == 3:
        continue
    else:
        print('Wrong data input')
        continue

    if current_player == player1:
        current_player = player2
        next_player = player1
    else:
        current_player = player1
        next_player = player2









