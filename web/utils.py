from flask import Flask, render_template, redirect, request, session
import requests

def get_artist_id(artist_name):
    """"""

    headers = {'Authorization':'Bearer ' + session['token']}
    payload = {
        'q': artist_name,
        'type': 'artist'
    }

    return requests.get('https://api.spotify.com/v1/search', params=payload, headers=headers).json()