from flask import Flask, render_template, redirect, request, session, jsonify
import requests

def get_id(input_name, input_type):
    """"""

    headers = {'Authorization':'Bearer ' + session['token']}
    payload = {
        'q': input_name,
        'type': input_type,
        'limit': 5
    }

    resp = requests.get('https://api.spotify.com/v1/search', params=payload, headers=headers).json()

    resp['input_type'] = input_type

    return resp

def get_genres():
    """"""

    headers = {'Authorization':'Bearer ' + session['token']}

    raw = requests.get('https://api.spotify.com/v1/recommendations/available-genre-seeds', headers=headers).json()
    genres = [(genre, genre.capitalize()) for genre in raw['genres']]
    genres[0] = ('', 'Genre (optional)')
    return genres

def get_key_list():
    """"""
    keys = [('','Select a Song Key'),('1','C'),('2','C#'),('3','D'),('4','D#'),('5','E'),('6','F'),('7','F#'),('8','G'),('9','G#'),('10','A'),('11','A#'),('12','B')]
    return keys

def get_modes():
    """"""
    keys = [('','Select Major or Minor Key'),('0','Minor'),('1','Major')]
    return keys

def get_user_id():
    """"""
    headers = {'Authorization':'Bearer ' + session['token']}
    raw = requests.get('https://api.spotify.com/v1/me', headers=headers).json()
    return raw['id']

def create_playlist(user_id):
    """"""
    headers = {
        'Authorization':'Bearer ' + session['token'],
        'Content-Type':'application/json'
        }

    data = '{"name": "My Playlist","public":false}'

    raw = requests.post(f'https://api.spotify.com/v1/users/{user_id}/playlists', headers=headers, data=data).json()

    return raw['id']

def add_songs_to_playlist(playlist_id, track_list):
    """"""
    headers = {
        'Authorization':'Bearer ' + session['token'],
        'Content-Type':'application/json'
        }

    params = {'uris':track_list}

    raw = requests.post(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers=headers, params=params).json()

    return raw

def delete_playlist(playlist_id):
    """"""
    headers = {
        'Authorization':'Bearer ' + session['token'],
        'Content-Type':'application/json'
        }

    raw = requests.delete(f'https://api.spotify.com/v1/playlists/{playlist_id}/followers', headers=headers)

    return raw


