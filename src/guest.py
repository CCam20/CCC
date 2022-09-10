class Guest:
    
    def __init__(self, name, money, fave_song):
        self.name = name
        self.money = money
        self.fave_song = fave_song

    def pay_fee(self, num):
        self.money -= num
        
    def pay_for_drink(self, num):
        self.money -= num