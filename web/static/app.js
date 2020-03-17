const $artist_search = $('#artist_search')
const $artist_search_results = $('#artist_search_results')
const $artist_search_button = $('#artist_search_button')

$artist_search_button.on("click", async function (evt) {

    evt.preventDefault();
        

    const seed_id = await getId($('#input1').val(), $("input[name='radio1']:checked").val()) 
    // $artist_search_results.append(seed_id.data.artists.items[0].id);

    if (seed_id.data.input_type == 'artist') {
        for (result of seed_id.data.artists.items) {
            link = `<input type="checkbox" name="${seed_id.data.input_type}" value="${result.id}" class="form-check-input">${result.name}<br>`
            $artist_search_results.append(link)
        }
        console.log("artist added")
    }

    if (seed_id.data.input_type == 'track') {
        for (result of seed_id.data.tracks.items) {

            link = `<input type="checkbox" name="${seed_id.data.input_type}" value="${result.id}" class="form-check-input">${result.name} - ${result.artists[0].name}<br>`
            $artist_search_results.append(link)
        }
        console.log("track added")
    }

    //resets form after return of artists/tracks
    $('#input1','')
    .val('');

    $("input[name='radio1']")
    .prop('checked', false);


})

async function getId (inputName, inputType) {

    resp = await axios.get('/search', {
        params: {
            q: inputName,
            type: inputType
        }
    })

    return resp
}


// {% for song in song_list %}
// <div class="container">
//     <iframe src="https://open.spotify.com/embed/track/{{song}}" width="400px" height="100px" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
// </div>
// {% endfor %}

// 'Content-Type':'application/x-www-form-urlencoded'


// @app.route("/user_auth")
// def get_spotify_auth():
//     """"""
//     code = request.args.get('code')
//     resp = requests.post('https://accounts.spotify.com/api/token', 
//         data ={
//             "grant_type": "authorization_code",
//             "code": code,
//             "redirect_uri": "http://localhost:5000/auth",
//             "client_id": CLIENT_ID,
//             "client_secret": CLIENT_SECRET
//         }).json()
//     token = resp['access_token']
//     refresh_token = resp['refresh_token']
//     session['token'] = token
//     session['refresh_token'] = refresh_token
//     session['user_id'] = get_user_id()
//     return redirect('/playground')