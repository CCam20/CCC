class Room:

    
    def __init__(self, room_number, max_space):
        self.room_number = room_number
        self.max_space = max_space
        self.songs =  []
        self.guests = []
        self.stock = []
        self.total_cash = 0

    def add_guest_to_room(self, guest):
            if len(self.guests) <5:
                self.guests.append(guest)

    def remove_guest_from_room(self, guest):
            self.guests.remove(guest)

    def add_song_to_room(self, song):
            self.songs.append(song)

    def clear_room(self):
        self.guests.clear()

    def check_for_fav_song(self, guest):
        for song in self.songs:
            if song.title == guest.fave_song:
                return 'Whoo!'
    
    def add_money_to_tab(self, num):
        self.total_cash += num

    def add_drinks_to_stock(self, drink):
        self.stock.append(drink)