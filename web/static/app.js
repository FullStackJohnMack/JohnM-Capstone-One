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

/* <ul>
    {% for result in resp['tracks'] %}
        <li><a href="{{result['external_urls']['spotify']}}" target="blank">{{result['artists'][0].name}} - {{result.name}}</a></li>
    {% endfor %}
</ul> */


/* <div class="form-group">  
{% if seed_1_type == 'artists' %}
    {% for result in seed_1_id[seed_1_type]['items'] %}
        <input type="checkbox" name="seed_artists" value="{{result['id']}}" class="form-check-input">{{result['name']}}<br>
    {% endfor %}
{% endif %}
</div>

<div class="form-group">  
{% if seed_2_type == 'artists' %}
    {% for result in seed_2_id[seed_2_type]['items'] %}
        <input type="checkbox" name="seed_artists" value="{{result['id']}}" class="form-check-input">{{result['name']}}<br>
    {% endfor %}
{% endif %}
</div>

<div class="form-group">  
{% if seed_3_type == 'artists' %}
    {% for result in seed_3_id[seed_3_type]['items'] %}
        <input type="checkbox" name="seed_artists" value="{{result['id']}}" class="form-check-input">{{result['name']}}<br>
    {% endfor %}
{% endif %}
</div>

<div class="form-group">  
{% if seed_4_type == 'artists' %}
    {% for result in seed_4_id[seed_4_type]['items'] %}
        <input type="checkbox" name="seed_artists" value="{{result['id']}}" class="form-check-input">{{result['name']}}<br>
    {% endfor %}
{% endif %}
</div>

<div class="form-group">  
{% if seed_5_type == 'artists' %}
    {% for result in seed_5_id[seed_5_type]['items'] %}
        <input type="checkbox" name="seed_artists" value="{{result['id']}}" class="form-check-input">{{result['name']}}<br>
    {% endfor %}
{% endif %}
</div>

<div class="form-group">  
{% if seed_1_type == 'tracks' %}
    {% for result in seed_1_id[seed_1_type]['items'] %}
        <input type="checkbox" name="seed_tracks" value="{{result['id']}}" class="form-check-input">{{result['name']}} - {{result['artists'][0]['name']}}<br>
    {% endfor %}
{% endif %}
</div>

<div class="form-group">  
{% if seed_2_type == 'tracks' %}
    {% for result in seed_2_id[seed_2_type]['items'] %}
        <input type="checkbox" name="seed_tracks" value="{{result['id']}}" class="form-check-input">{{result['name']}} - {{result['artists'][0]['name']}}<br>
    {% endfor %}
{% endif %}
</div>

<div class="form-group">  
{% if seed_3_type == 'tracks' %}
    {% for result in seed_3_id[seed_3_type]['items'] %}
        <input type="checkbox" name="seed_tracks" value="{{result['id']}}" class="form-check-input">{{result['name']}} - {{result['artists'][0]['name']}}<br>
    {% endfor %}
{% endif %}
</div>

<div class="form-group">  
{% if seed_4_type == 'tracks' %}
    {% for result in seed_4_id[seed_4_type]['items'] %}
        <input type="checkbox" name="seed_tracks" value="{{result['id']}}" class="form-check-input">{{result['name']}} - {{result['artists'][0]['name']}}<br>
    {% endfor %}
{% endif %}
</div>

<div class="form-group">  
{% if seed_5_type == 'tracks' %}
    {% for result in seed_5_id[seed_5_type]['items'] %}
        <input type="checkbox" name="seed_tracks" value="{{result['id']}}" class="form-check-input">{{result['name']}} - {{result['artists'][0]['name']}}<br>
    {% endfor %}
{% endif %}
</div> */}
// genres = get_genres()
//         keys = get_key_list()
//         modes = get_modes()

// seed_2_type = f'{form.radio2.data}s'
// seed_3_type = f'{form.radio3.data}s'
// seed_4_type = f'{form.radio4.data}s'
// seed_5_type = f'{form.radio5.data}s'

// seed_2_id = get_id(form.input2.data, form.radio2.data)
// seed_3_id = get_id(form.input3.data, form.radio3.data)
// seed_4_id = get_id(form.input4.data, form.radio4.data)
// seed_5_id = get_id(form.input5.data, form.radio5.data)


// def get_id(input_name, input_type):
//     """"""

//     headers = {'Authorization':'Bearer ' + session['token']}
//     payload = {
//         'q': input_name,
//         'type': input_type
//     }

//     return requests.get('https://api.spotify.com/v1/search', params=payload, headers=headers).json()