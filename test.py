from bottle import Bottle, route, request, static_file, get, run
import lyricwikia
from gtts import gTTS
from tempfile import TemporaryFile
import random
import os
import time


@route('/')
def audio():
    return '''
        <form action="/mada.mp3"method="post">
            Song Name: <input name="name" type="text" />
            Song Artist: <input name="artist" type="text" />
            <input value="Submit" type="submit" />
        </form>
    '''


@route('/<filename>', method='POST')
def getaudio(filename):
    name = request.forms.get('name')
    artist = request.forms.get('artist')
    lyrics = lyricwikia.get_lyrics(artist, name)
    tts = gTTS(text=lyrics, lang='en', slow=False)
    tts.save('./file.mp3')
    return static_file(filename, root='./file.mp3', mimetype='audio/mpeg')


run(host='localhost', port=8080, debug=True)
