import unittest
from src.guest import Guest 
from src.songs import Songs 
from src.room import Room
from src.drinks import Drinks

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest('Mona Yvonne', 100,'Around the world' )
        self.guest2 = Guest('Conor Upton', 50, 'Smash it up')
        self.room1 = Room(1, 5)
        self.room2 = Room(2, 5)
        self.song1 = Songs('Around the world', 'Daft Punk')
        self.song2 = Songs('Master of Puppets', 'Metallica')
        self.song3 = Songs('Smash it up', 'The Dammed')

    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.assertEqual(1 ,len(self.room1.guests))

    def test_remove_guests_from_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.remove_guest_from_room(self.guest1)
        self.assertEqual(1 ,len(self.room1.guests))

    def test_remove_all_guests_from_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.clear_room()
        self.assertEqual(0 ,len(self.room1.guests))

    def test_is_enough_space_in_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.assertGreaterEqual(5,len(self.room1.guests))

    def test_pay_fee(self):
        self.guest1.pay_fee(10)
        self.assertEqual(90, self.guest1.money)

    def test_can_add_to_room_total(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_money_to_tab(10)
        self.assertEqual(10, self.room1.total_cash)