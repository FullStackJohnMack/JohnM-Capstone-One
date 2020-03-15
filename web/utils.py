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

