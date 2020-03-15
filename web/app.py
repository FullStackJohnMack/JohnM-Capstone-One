from flask import Flask, render_template, redirect, request, session
import requests, base64
from access import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from forms import SearchForm
from utils import get_id, get_genres, get_key_list, get_modes

app = Flask(__name__)
app.secret_key = "password"

@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())
    

@app.route("/")
def get_homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route("/spotify/auth")
def get_spotify_auth():
    """"""
    code = request.args.get('code')
    resp = requests.post('https://accounts.spotify.com/api/token', 
        data ={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": "http://localhost:5000/spotify/auth",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        }).json()
    token = resp['access_token']
    refresh_token = resp['refresh_token']
    session['token'] = token
    session['refresh_token'] = refresh_token
    return redirect('/search')

@app.route("/search", methods=["GET", "POST"])
def search_spotify():
    """"""

    form = SearchForm()

    if form.validate_on_submit():

        seed_1_id = get_id(form.input1.data, form.radio1.data)
        seed_2_id = get_id(form.input2.data, form.radio2.data)
        seed_3_id = get_id(form.input3.data, form.radio3.data)
        seed_4_id = get_id(form.input4.data, form.radio4.data)
        seed_5_id = get_id(form.input5.data, form.radio5.data)

        seed_1_type = f'{form.radio1.data}s'
        seed_2_type = f'{form.radio2.data}s'
        seed_3_type = f'{form.radio3.data}s'
        seed_4_type = f'{form.radio4.data}s'
        seed_5_type = f'{form.radio5.data}s'

        genres = get_genres()
        keys = get_key_list()
        modes = get_modes()

        return render_template("search_results.html", genres=genres, keys=keys, modes=modes, seed_1_id=seed_1_id, seed_1_type=seed_1_type, seed_2_id=seed_2_id, seed_2_type=seed_2_type, seed_3_id=seed_3_id, seed_3_type=seed_3_type,seed_4_id=seed_4_id, seed_4_type=seed_4_type,seed_5_id=seed_5_id, seed_5_type=seed_5_type)

    return render_template("search.html", form=form)


@app.route("/search/seed", methods=['POST'])
def show_recommendations():
    """"""

    headers = {'Authorization':'Bearer ' + session['token']}
    
    payload = {

        }

    if request.form.get('seed_artists'):
        artist_list = [f'{artist},' for artist in request.form.getlist('seed_artists')];
        payload['seed_artists'] = artist_list

    for id in request.form.getlist('seed_tracks'):
        payload['seed_tracks'] += f"{id},"

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

    return render_template("seed_results.html", resp=resp)



# https://api.spotify.com/v1/recommendations
# http://127.0.0.1:5000



# limit
# market
# seed_artists
# seed_genres
# seed_tracks
# min_acousticness
# max_acousticness
# target_acousticness
# min_danceability
# max_danceability
# target_danceability
# min_duration
# max_duration
# target_duration
# min_energy
# max_energy
# target_energy
# min_instrumentalness
# max_instrumentalness
# arget_instrumentalness
# min_key
# max_key
# target_key
# min_liveness
# max_liveness
# target_liveness
# min_loudness
# max_loudness
# target_loudness
# min_mode
# max_mode
# target_mode
# min_popularity
# max_popularity
# target_popularity
# min_speechiness
# max_speechiness
# target_speechiness
# min_tempo
# max_tempo
# target_tempo
# min_time_signature
# max_time_signature
# target_time_signature
# min_valence
# max_valence
# target_valence
