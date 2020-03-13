from flask import Flask, render_template, redirect, request, session
import requests, base64
from access import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from forms import SearchForm
from utils import get_id

app = Flask(__name__)
app.secret_key = "password"

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
        # seed_3_id = get_id(form.input3.data, form.radio3.data)
        # seed_4_id = get_id(form.input4.data, form.radio4.data)
        # seed_5_id = get_id(form.input5.data, form.radio5.data)

        seed_1_type = f'{form.radio1.data}s'
        seed_2_type = f'{form.radio2.data}s'
        # seed_3_type = f'{form.radio3.data}s'
        # seed_4_type = f'{form.radio4.data}s'
        # seed_5_type = f'{form.radio5.data}s'

        return render_template("search_results.html", seed_1_id=seed_1_id, seed_1_type=seed_1_type, seed_2_id=seed_2_id, seed_2_type=seed_2_type)

    return render_template("search.html", form=form)


@app.route("/search/seed", methods=['POST'])
def show_recommendations():
    """"""

    seed_artists = ""
    seed_tracks = ""
    
    for id in request.form.getlist('seed_artists'):
        seed_artists += f"{id},"

    for id in request.form.getlist('seed_tracks'):
        seed_tracks += f"{id},"


    headers = {'Authorization':'Bearer ' + session['token']}
    payload = {
            'seed_artists': seed_artists,
            'seed_tracks': seed_tracks,
            'limit': 100
        }

    resp = requests.get('https://api.spotify.com/v1/recommendations', params=payload, headers=headers).json()

    return render_template("seed_results.html", resp=resp, seed_artists=seed_artists, seed_tracks=seed_tracks)




# , seed_3_id=seed_3_id, seed_4_id=seed_4_id,seed_5_id=seed_5_id
# , ,seed_3_type=seed_3_type, seed_4_type=seed_4_type,seed_5_type=seed_5_type



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
