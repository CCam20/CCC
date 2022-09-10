import unittest
from src.guest import Guest
from src.room import Room
from src.songs import Songs
from src.drinks import Drinks


class TestSongs(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest('Mona Yvonne', 100,'Around the world' )
        self.guest2 = Guest('Conor Upton', 50, 'Smash it up')
        self.room1 = Room(1, 6)
        self.room2 = Room(2, 6)
        self.song1 = Songs('Around the world', 'Daft Punk')
        self.song2 = Songs('Master of Puppets', 'Metallica')
        self.song3 = Songs('Smash it up', 'The Dammed')

    def test_add_song_to_room(self):
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song2)
        self.assertEqual(2,len(self.room1.songs))