import flask
import requests
import os
import json
from dotenv import load_dotenv, find_dotenv
import random


app = flask.Flask(__name__)

load_dotenv(find_dotenv())

@app.route('/')
def index():
    
    data = {
        'grant_type': 'client_credentials',
        'client_id': os.environ['CLIENT_ID'],
        'client_secret': os.environ['CLIENT_SECRET'],
    }   
    
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    
    response = requests.post(AUTH_URL, data)
    response = response.json()
    access_token = response['access_token']
    
    artist = ['3TVXtAsR1Inumwj472S9r4', '7rkW85dBwwrJtlHRDkJDAC', '0Y5tJX1MQlPlqiwlOH1tJY']  #Drake, NAV, Travis Scott
    
    randomArtist = random.choice(artist)
    
    if randomArtist == '3TVXtAsR1Inumwj472S9r4':
        BASE_URL = 'https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4/top-tracks?market=US'
    
    elif randomArtist =='7rkW85dBwwrJtlHRDkJDAC':
        BASE_URL = 'https://api.spotify.com/v1/artists/7rkW85dBwwrJtlHRDkJDAC/top-tracks?market=US'
    
    elif randomArtist == '0Y5tJX1MQlPlqiwlOH1tJY':
        BASE_URL = 'https://api.spotify.com/v1/artists/0Y5tJX1MQlPlqiwlOH1tJY/top-tracks?market=US'

    headers = {
        'Authorization': 'Bearer {token}'.format(token = access_token)
    }   


    response = requests.get(BASE_URL, headers=headers)
    r = response.json()
    image = json.dumps(r['tracks'][1]['album']['images'][0]['url'])
    image = image.strip('"')
    songName = json.dumps(r['tracks'][1]['name'], indent=4)
    songName = songName.strip('"')
    songURL = json.dumps(r['tracks'][1]['uri'], indent=4)
    songURL = songURL.strip('"')
    artistName = json.dumps(r['tracks'][1]['album']['artists'][0]['name'], indent=4)
    
    if songName == 'POPSTAR (feat. Drake)':
        songName = 'Popstar'
    
    GENIUS_URL = 'http://api.genius.com/search'
    params = {'q': songName}
    headers = {'Authorization': 'Bearer TBSlj-I1f2ymnQuWQqMV8fVJvlmaHRG6f9d1tZuBIWDdKjHyCDvGroKpjCUwCGy8'}
    
    response = requests.get(GENIUS_URL, params=params, headers=headers)
    g = response.json()
    
    if songName == 'Turks (with Gunna & ft. Travis Scott)':
        lyricsURL = json.dumps(g['response']['hits'][1]['result']['url'], indent=4) 
    
    elif songName == 'Popstar':
        lyricsURL = json.dumps(g['response']['hits'][0]['result']['url'], indent=4)
        
    elif songName == 'Goosebumps - Remix':
        lyricsURL = json.dumps(g['response']['hits'][6]['result']['url'], indent=4)
       
    lyricsURL = lyricsURL.strip('"')

    return flask.render_template(
        "index.html",
        relevent_image= image,
        song_name= songName,
        song_url= songURL,
        artist_name = artistName,
        lyrics_url = lyricsURL)
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
    )