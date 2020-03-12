from flask import Flask, render_template, redirect, request, session
import requests, base64
from access import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from forms import SearchForm

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

        
        headers = {'Authorization':'Bearer ' + session['token']}
        payload = {
            'q': form.input1.data,
            'type': form.radio1.data
        }

        input_1_type = f'{form.radio1.data}s'

        resp = requests.get('https://api.spotify.com/v1/search', params=payload, headers=headers).json()
        return render_template("results.html", resp=resp, input_1_type=input_1_type)

    return render_template("search.html", form=form)


@app.route("/search/seed", methods=['POST'])
def show_recommendations():
    """"""

    data = request.form.getlist('input_1')


    headers = {'Authorization':'Bearer ' + session['token']}
    payload = {
            'seed_artists': data[0]
        }


    resp = requests.get('https://api.spotify.com/v1/recommendations', params=payload, headers=headers).json()

    return render_template("results1.html", resp=resp)


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
