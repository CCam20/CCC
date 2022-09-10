from re import S
import unittest
from src.guest import Guest
from src.room import Room
from src.songs import Songs
from src.drinks import Drinks

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest('Mona Yvonne', 100,'Around the world' )
        self.guest2 = Guest('Conor Upton', 50, 'Smash it up')
        self.room1 = Room(1, 6)
        self.room2 = Room(2, 6)
        self.song1 = Songs('Around the world', 'Daft Punk')
        self.song2 = Songs('Master of Puppets', 'Metallica')
        self.song3 = Songs('Smash it up', 'The Dammed')
        self.drink1 = Drinks('Budweiser', 4.00)
        self.drink2 = Drinks("Buckfast",2.50)
        self.drink3 = Drinks('Jack Daniels',3.50) 



    def test_guest_has_name(self):
        self.assertEqual('Mona Yvonne', self.guest1.name)
    
    def test_guest_has_money(self):
        self.assertEqual(100, self.guest1.money)

    def test_fav_song(self):
        self.room1.add_song_to_room(self.song1)
        self.room1.check_for_fav_song(self.guest1)
        reaction = self.room1.check_for_fav_song(self.guest1)
        self.assertEqual("Whoo!", reaction)

    def test_can_buy_drink(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_drinks_to_stock(self.drink2)
        self.room1.add_money_to_tab(self.drink2.price)
        self.guest1.pay_for_drink(self.drink2.price)
        self.assertEqual(self.room1.total_cash, 2.50)
        # self.assertEqual(self.room1,)
        self.assertEqual(self.guest1.money, 97.50)


        