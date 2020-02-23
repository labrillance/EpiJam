class player:
    def __init__(self):
        self.name = ""
        self.color = 0
        self.gold = 0
        self.oil = 0
        self.iron = 0
        self.bases = bases()
        self.own = []

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
        self.vitesse = 0
        self.power = 0
        self.posx = 0
        self.posy = 0