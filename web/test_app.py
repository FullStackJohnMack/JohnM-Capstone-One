""" Tests app.py file
    Unable to test get_spotify_user_auth, remove_playlist, and logout_user 
    because no API based user login method is allowed on Spotify's API
"""

from unittest import TestCase
from app import app
from utils import *

app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False



# ------------------------INTEGRATION TESTS------------------------
class IntegrationTests(TestCase):



# ------------TESTS FOR DIRECT VIEWS------------

    def test_get_homepage(self):
        """Tests view for home page."""
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<a class="btn btn-primary" href="/auth">Start Search</a>',html)

    def test_get_user_auth_page(self):
        """Tests when user visits /user_auth directly."""
        with app.test_client() as client:
            resp = client.get('/user_auth', follow_redirects = True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<a class="btn btn-primary" href="/auth">Start Search</a>',html)

    def test_get_search_page(self):
        """Tests when user visits /search directly."""
        with app.test_client() as client:
            resp = client.get('/search', follow_redirects = True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<a class="btn btn-primary" href="/auth">Start Search</a>',html)

    def test_get_delete(self):
        """Tests when user visits /delete directly."""
        with app.test_client() as client:
            resp = client.post('/delete')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 405)
            session.clear()

    def test_go_to_search_page_without_auth(self):
        """Tests when a user visits /playground directly (and not authenticated at either level)."""
        with app.test_client() as client:
            resp = client.get('/playground')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 302)
            self.assertIn('You should be redirected automatically to target URL: <a href="/">',html)
            session.clear()




# ------------TESTS FOR AUTHENTICATION / AUTHORIZATION ------------

    def test_get_spotify_auth(self):
        """Tests for app level login on server side."""
        with app.test_client() as client:
            resp = client.get('/auth')
            html = resp.get_data(as_text=True)
            self.assertIn('token', session)
            self.assertEqual(resp.status_code, 302)
            session.clear()




# ------------TESTS NAV LINKS ------------

    def test_go_to_search_page(self):
        """Tests when a user clicks the "Search" link."""
        with app.test_client() as client:
            resp = client.get('/auth', follow_redirects = True)
            html = resp.get_data(as_text=True)
            self.assertIn('token', session)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Search the Playground</button>',html)
            session.clear()




# ------------TESTS FOR OUR API------------

    def test_artist_or_track_search_for_artist(self):
        """Tests our API for an artist search."""
        with app.test_client() as client:
            resp = client.get('/auth')
            artist = 'Calibretto'
            type = 'artist'
            resp = get_id(artist,type)
            self.assertIn('Calibretto 13', resp['artists']['items'][0]['name'])

    def test_artist_or_track_search_for_track(self):
        """Tests our API for a track search."""
        with app.test_client() as client:
            client.get('/auth')
            track = "cmon girl"
            type = 'track'
            resp = get_id(track,type)
            self.assertIn("C'mon Girl", resp['tracks']['items'][0]['name'])




# ------------TESTS FOR SEED SEARCHES------------

    def test_show_recommendations_testing_genre(self):
        """Tests seeding based on genre."""
        with app.test_client() as client:
            client.get('/auth')
            resp = client.post(
                        '/seed',
                        data={'seed_genre': 'punk-rock'},
                        follow_redirects = True
                    )
            html = resp.get_data(as_text=True)
            self.assertIn('<iframe src="https://open.spotify.com/embed/track/',html)

    def test_show_recommendations_testing_artist(self):
        """Tests seeding based on artist."""
        with app.test_client() as client:
            client.get('/auth')
            resp = client.post(
                        '/seed',
                        data={'artist': '3KKiTDneH2x2sLtVPnTSOh'},
                        follow_redirects = True
                    )
            html = resp.get_data(as_text=True)
            self.assertIn('<iframe src="https://open.spotify.com/embed/track/',html)

    def test_show_recommendations_testing_track(self):
        """Tests seeding based on track."""
        with app.test_client() as client:
            client.get('/auth')
            resp = client.post(
                        '/seed',
                        data={'track': '3HVUvLe8yJ4WXLNMmfuisL'},
                        follow_redirects = True
                    )
            html = resp.get_data(as_text=True)
            self.assertIn('<iframe src="https://open.spotify.com/embed/track/',html)

    def test_show_recommendations_testing_several(self):
        """Tests seeding based on several seeds including artist, track, genre, and more."""
        with app.test_client() as client:
            client.get('/auth')
            resp = client.post(
                        '/seed',
                        data={
                            'track': '3HVUvLe8yJ4WXLNMmfuisL',
                            'artist': '3KKiTDneH2x2sLtVPnTSOh',
                            'seed_genre': 'punk-rock',
                            'acousticness': 1,
                            'include_tempo': 1,
                            'tempo': 200
                        },
                        follow_redirects = True
                    )
            html = resp.get_data(as_text=True)
            self.assertIn('<iframe src="https://open.spotify.com/embed/track/',html)




# ------------TESTS FOR LOGOUT------------

    def test_logout(self):
        """Tests when user clicks the Logout link"""
        with app.test_client() as client:
            client.get('/auth')
            session['token'] = 'test_token'
            session['refresh_token'] = 'test_refresh_token'
            session['user_id'] = 'test_user_id'
            test_user_id = 'test_user_id'
            self.assertEqual(test_user_id,session.get('user_id'))
            self.assertEqual(session['user_id'],'test_user_id')
            session.clear()
            self.assertNotEqual(test_user_id,session.get('user_id'))