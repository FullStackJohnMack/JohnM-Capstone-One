from flask import Flask, render_template, redirect, request, session
import requests, base64
from access import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SECRET_KEY, B64_CODE
from forms import SearchForm
from utils import get_id, get_genres, get_key_list, get_modes, get_user_id, create_playlist, add_songs_to_playlist, delete_playlist
from flask_wtf.csrf import CSRFProtect
import pdb

csrf = CSRFProtect()

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

csrf.init_app(app)

@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())
    

@app.route("/")
def get_homepage():
    """Show homepage."""

    

    return render_template("index.html")


@app.route("/auth")
def get_spotify_auth():
    """"""

    headers = {
        'Authorization':'Basic {}'.format(B64_CODE)
    }

    print(headers)

    data = {
        'grant_type': 'client_credentials'
    }

    resp = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data).json()
 
    token = resp['access_token']
    session['token'] = token
    
    return redirect('/playground')

@app.route("/playground")
def go_to_search_page():
    """"""
    genres = get_genres()
    keys = get_key_list()
    modes = get_modes()

    return render_template("search.html", genres=genres, keys=keys, modes=modes)


@app.route("/search", methods=["GET"])
def artist_or_track_search():
    """API endpoint that accepts an artist or track query and type (artist or track) and returns a list of tuples with Spotify ID and artist or track name. [("Uesfsz...dsd","artist"),("TDSdsd...dfd","track")]"""

    artist = request.args.get('q')
    type = request.args.get('type')
    
    resp = get_id(artist,type)

    return resp


@app.route("/seed", methods=['POST'])
def show_recommendations():
    """"""

    headers = {'Authorization':'Bearer ' + session['token']}
    
    payload = {

        }

    if request.form.get('artist'):
        artist_list = [f'{artist},' for artist in request.form.getlist('artist')];
        payload['seed_artists'] = artist_list

    for id in request.form.getlist('track'):
        track_list = [f'{track},' for track in request.form.getlist('track')];
        payload['seed_tracks'] = track_list

    if request.form.get('seed_genre'):
        payload['seed_genres'] = request.form.get('seed_genre')

    if request.form.get('acousticness'):
        payload['target_acousticness'] = 1.0

    if request.form.get('danceability'):
        payload['target_danceability'] = 1.0

    if request.form.get('energy'):
        payload['target_energy'] = 1.0

    if request.form.get('instrumentalness'):
        payload['target_instrumentalness'] = 1.0

    if request.form.get('liveness'):
        payload['target_liveness'] = 1.0

    if request.form.get('speechiness'):
        payload['target_speechiness'] = 1.0

    if request.form.get('valence'):
        payload['target_valence'] = 1.0

    if request.form.get('include_min_duration'):
        payload['min_duration_ms'] = int(request.form.get('min_duration'))

    if request.form.get('include_max_duration'):
        payload['max_duration_ms'] = int(request.form.get('max_duration'))

    if request.form.get('key'):
        payload['target_key'] = int(request.form.get('key'))

    if request.form.get('include_loudness'):
        payload['target_loudness'] = float(request.form.get('loudness'))

    if request.form.get('mode'):
        payload['target_mode'] = int(request.form.get('mode'))

    if request.form.get('include_popularity'):
        payload['target_popularity'] = int(request.form.get('popularity'))
    
    if request.form.get('include_tempo'):
        payload['target_tempo'] = float(request.form.get('tempo'))
    
    if request.form.get('include_time_sig'):
        payload['target_time_signature'] = int(request.form.get('time_sig'))

   

    resp = requests.get('https://api.spotify.com/v1/recommendations', params=payload, headers=headers).json()
    
    track_list = []


    for track in resp['tracks']:
        track_list.append(track['id'])


    # session['playlist_id'] = create_playlist(session['user_id'])
    # add_songs_to_playlist(session['playlist_id'], final)

    return render_template("results.html", resp=resp, track_list=track_list)


@app.route("/delete", methods=["GET"])
def unfollow_playlist():
    """"""
    
    delete_playlist(session['playlist_id'])

    return redirect('/playground')


# playlist_id=session['playlist_id']


# @app.route("/user_auth")
# def get_spotify_user_auth():
#     """"""
#     code = request.args.get('code')
#     resp = requests.post('https://accounts.spotify.com/api/token', 
#         data ={
#             "grant_type": "authorization_code",
#             "code": code,
#             "redirect_uri": "http://localhost:5000/user_auth",
#             "client_id": CLIENT_ID,
#             "client_secret": CLIENT_SECRET
#         }).json()
#     token = resp['access_token']
#     refresh_token = resp['refresh_token']
#     session['token'] = token
#     session['refresh_token'] = refresh_token
#     session['user_id'] = get_user_id()
#     return redirect('/seed')

