const $artist_search = $('#artist_search')
const $artist_search_results = $('#artist_search_results')
const $artist_search_button = $('#artist_search_button')
const $seed_submit_button = $('#seed_submit_button')


/*
* Handles click on 'Add Search Results' button
*
*/

$artist_search_button.on("click", async function (evt) {
    
    evt.preventDefault();
    
    //removes an alert when an artist or track isn't found
    $("#artist_not_found_alert").remove()
    
    //renders an error message for user if neither the artist nor song button is selected when searching an artist or track
    if ($("input[name='radio1']:checked").val() == undefined) {
        $artist_search.append('<div id="radio_alert" class="alert alert-danger mt-4" role="alert">Select either "Artist" or "Song" along with a query when trying to Add Search Results</div>');
        return
    }
    
    //sends artist/track search query and type to our API route
    const seed_id = await getId($('#input1').val(), $("input[name='radio1']:checked").val())

    //renders content if an artist is returned from Spotify
    if (seed_id.data.input_type == 'artist') {

        //tells user if their search didn't find anything
        if (seed_id.data.artists.total == 0) {
            message = '<div id="artist_not_found_alert" class="alert alert-warning mt-4" role="alert">Artist not found</div>'
            $artist_search.append(message)
        }
        for (result of seed_id.data.artists.items) {
            link = `<label class="btn btn-outline-success btn-sm m-2"><input type="checkbox" name="${seed_id.data.input_type}" value="${result.id}" class="form-check-input">${result.name}</label>`
            $artist_search_results.append(link)
        }
    }

    //renders content if a track is returned from Spotify
    if (seed_id.data.input_type == 'track') {

        //tells user if their search didn't find anything
        if (seed_id.data.tracks.total == 0) {
            message = '<div id="artist_not_found_alert" class="alert alert-warning mt-4" role="alert">Song not found</div>'
            $artist_search.append(message)
        }
        for (result of seed_id.data.tracks.items) {
            link = `<label class="btn btn-outline-success btn-sm m-2"><input type="checkbox" name="${seed_id.data.input_type}" value="${result.id}" class="form-check-input">${result.name} - ${result.artists[0].name}</label>`
            $artist_search_results.append(link)
        }
    }

    //resets form input after artist/track search form submission
    $('#input1','')
    .val('');

    //resets radio buttons for artist and track search on form on successful form submission
    $("input[name='radio1']")
    .prop('checked', false);
    $("label")
    .removeClass('active');

    //removes alert that tells user that either artist or track radio button selected on artist/track search
    $("#radio_alert").remove()
})



/*
* Calls our artist/track search route and returns a Spotify UID for either an artist or track
*
*/
async function getId (inputName, inputType) {

    resp = await axios.get('/search', {
        params: {
            q: inputName,
            type: inputType
        }
    })
    return resp
}