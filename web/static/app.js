const $artist_search = $('#artist_search')
const $artist_search_results = $('#artist_search_results')
const $artist_search_button = $('#artist_search_button')
const $seed_submit_button = $('#seed_submit_button')

$artist_search_button.on("click", async function (evt) {

    evt.preventDefault();

    $("#artist_not_found_alert").remove()

    if ($("input[name='radio1']:checked").val() == undefined) {
        $artist_search.append('<div id="radio_alert" class="alert alert-danger mt-4" role="alert">Select either "Artist" or "Song" along with a query when trying to Add Search Results</div>');
        return
    }

    const seed_id = await getId($('#input1').val(), $("input[name='radio1']:checked").val()) 


    if (seed_id.data.input_type == 'artist') {
        if (seed_id.data.artists.total == 0) {
            message = '<div id="artist_not_found_alert" class="alert alert-warning mt-4" role="alert">Artist not found</div>'
            $artist_search.append(message)
        }

        for (result of seed_id.data.artists.items) {
            link = `<label class="btn btn-outline-success btn-sm m-2"><input type="checkbox" name="${seed_id.data.input_type}" value="${result.id}" class="form-check-input">${result.name}</label>`
            $artist_search_results.append(link)
        }
    }

    if (seed_id.data.input_type == 'track') {
        if (seed_id.data.tracks.total == 0) {
            message = '<div id="artist_not_found_alert" class="alert alert-warning mt-4" role="alert">Song not found</div>'
            $artist_search.append(message)
        }

        for (result of seed_id.data.tracks.items) {
            link = `<label class="btn btn-outline-success btn-sm m-2"><input type="checkbox" name="${seed_id.data.input_type}" value="${result.id}" class="form-check-input">${result.name} - ${result.artists[0].name}</label>`
            $artist_search_results.append(link)
        }
    }

    

    

    //resets form after return of artists/tracks
    $('#input1','')
    .val('');

    $("input[name='radio1']")
    .prop('checked', false);

    $("label")
    .removeClass('active');

    $("#radio_alert").remove()

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