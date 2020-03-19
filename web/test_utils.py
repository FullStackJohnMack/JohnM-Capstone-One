""" Tests utils.py file
    Unable to test get_user_id, create_playlist, add_songs_to_playlist, 
    and delete_playlist as they require a user login which Spotify doesn't 
    via their API.
"""

from unittest import TestCase
from app import app
from utils import *


# ------------------------UNIT TESTS------------------------

class UnitTests(TestCase):

    def test_get_key_list(self):
        """Test to get list of song keys"""
        self.assertEqual(get_key_list(),[('','Select a Song Key'),('1','C'),('2','C#'),('3','D'),('4','D#'),('5','E'),('6','F'),('7','F#'),('8','G'),('9','G#'),('10','A'),('11','A#'),('12','B')])

    def test_get_modes(self):
        """Test to get list of musical modes"""
        self.assertEqual(get_modes(),[('','Select Major or Minor Key'),('0','Minor'),('1','Major')])



# ------------------------INTEGRATION TESTS------------------------
class IntegrationTests(TestCase):

    def test_get_id_artist(self):
        """Tests call to Spotify's API for artist search"""
        with app.test_client() as client:
            client.get('/auth')
            input_name = 'Calibretto'
            input_type = 'artist'
            resp = get_id(input_name,input_type)
            session.clear()
            self.assertEqual(resp['artists']['items'][0]['name'],'Calibretto 13')

    def test_get_id_artist_not_found(self):
        """Tests call to Spotify's API for artist search when artist cannot be found"""
        with app.test_client() as client:
            client.get('/auth')
            input_name = '!@#$%^^&&*'
            input_type = 'artist'
            resp = get_id(input_name,input_type)
            session.clear()
            self.assertEqual(resp['artists']['total'],0)

    def test_get_id_track(self):
        """Tests call to Spotify's API for track search"""
        with app.test_client() as client:
            client.get('/auth')
            input_name = 'cmon girl'
            input_type = 'track'
            resp = get_id(input_name,input_type)
            session.clear()
            self.assertEqual(resp['tracks']['items'][0]['name'],"C'mon Girl")

    def test_get_id_track_not_found(self):
        """Tests call to Spotify's API for track search when track cannot be found"""
        with app.test_client() as client:
            client.get('/auth')
            input_name = '!'
            input_type = 'track'
            resp = get_id(input_name,input_type)
            session.clear()
            self.assertEqual(resp['tracks']['total'],0)

    def test_get_id_no_input_type(self):
        """Tests call to Spotify's API for track search when track cannot be found"""
        with app.test_client() as client:
            client.get('/auth')
            input_name = '!'
            input_type = None
            resp = get_id(input_name,input_type)
            session.clear()
            self.assertEqual(resp['error']['status'],400)

    def test_get_genres(self):
        """Tests call to Spotify's API to get list of genres"""
        with app.test_client() as client:
            client.get('/auth')
            resp = get_genres()
            session.clear()
            self.assertEqual(('afrobeat','Afrobeat'),resp[1])