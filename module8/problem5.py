#Zaineb Bonilla
#11/21/2023
#Problem 5

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses

    def itemspicked(self,weapons,weaknesses):
        if "rope" in weapons and "coat" in weapons and "first aid kit" in weapons and "slow" not in weaknesses:
            print("can climb mountain")
        if "pan" in weapons and "groceries" in weapons and "small" not in weaknesses:
            print("can cook a meal")
        if "pen" in weapons and "paper" in weapons and "idea" in weapons and "confusion" not in weaknesses:
            print("can write a book")

player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)
player1.itemspicked(player1.weapons, player1.weaknesses)