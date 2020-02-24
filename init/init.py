class player:
    def __init__(self):
        self.name = ""
        self.color = 0
        self.gold = 0
        self.oil = 0
        self.iron = 0
        self.bases = bases()
        self.fusee = fusee()
        self.own = []
        self.price_fusee_atk = []
        self.price_fusee_atk.append(10)
        self.price_fusee_atk.append(50)
        self.level = 1
        self.position = 0

class planete:
    def __init__(self):
        self.name = ""
        self.gold = 0
        self.oil = 0
        self.iron = 0
        self.x = 0
        self.y = 0
        self.long = 0
        self.larg = 0
        self.colonise = 0
        self.defenselvl = 1
        self.valeur = 0

class bases:
    def __init__(self):
        self.prop = ""
        self.image = 0
        self.rect = 0
        self.posx = 0
        self.posy = 0

class fusee:
    def __init__(self):
        self.status = 0
        self.shild = 0
        self.atk = 0
        self.posx = 0
        self.posy = 0

class info:
    def __init__(self):
        self.name = ""
        self.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        self.gold = 0
        self.iron = 0
        self.oil = 0
        self.buy = 0
        self.dist = 0
        self.level = 0
