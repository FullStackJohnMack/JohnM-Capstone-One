from flask import Flask, render_template, redirect, request, session
import requests

def get_id(input_name, input_type):
    """"""

    headers = {'Authorization':'Bearer ' + session['token']}
    payload = {
        'q': input_name,
        'type': input_type
    }

    return requests.get('https://api.spotify.com/v1/search', params=payload, headers=headers).json()

def get_genres():
    """"""

    headers = {'Authorization':'Bearer ' + session['token']}

    raw = requests.get('https://api.spotify.com/v1/recommendations/available-genre-seeds', headers=headers).json()
    genres = [(genre, genre.capitalize()) for genre in raw['genres']]
    genres[0] = ('No Genre', 'Genre (optional)')
    return genres