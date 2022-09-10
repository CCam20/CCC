import unittest
from src.guest import Guest
from src.room import Room
from src.songs import Songs
from src.drinks import Drinks


class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest('Mona Yvonne', 100,'Around the world' )
        self.room1 =  Room(1, 6)
        self.song1 =  Songs('Around the world', 'Daft Punk')
        self.drink1 = Drinks('Budweiser', 4.00)
        self.drink2 = Drinks("Buckfast",2.50)
        self.drink3 = Drinks('Jack Daniels',3.50)

    def test_can_add_to_bartab(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_money_to_tab(10)
        self.assertEqual(10, self.room1.total_cash)

    def test_can_add_drinks_to_stock(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_drinks_to_stock(self.drink1)
        self.assertEqual(1, len(self.room1.stock))

    def test_cust_can_buy_drinks(self):
        self.room1.add_guest_to_room(self.guest1)

    def test_drink_has_name(self):
        self.assertEqual('Budweiser', self.drink1.name)

    def test_drink_has_price(self):
        self.assertEqual(4.00, self.drink1.price)

