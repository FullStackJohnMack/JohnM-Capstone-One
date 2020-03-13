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