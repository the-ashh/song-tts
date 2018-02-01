from bottle import Bottle, route, request, static_file, run
import lyricwikia
from gtts import gTTS
from tempfile import TemporaryFile
import random
import os

'''
@route('/login', method='POST')
def do_login():
    name = request.forms.get('name')
    artist = request.forms.get('artist')
    lyrics = lyricwikia.get_lyrics(artist, name)
    tts = gTTS(text=lyrics, lang='en', slow=False)
    f = TemporaryFile()
    tts.write_to_fp(f)
    audio(random.randrange(999))
'''

@route('/audio')
def audio():
    return '''
        <form action="/audio" method="post">
            Song Name: <input name="name" type="text" />
            Song Artist: <input name="artist" type="text" />
            <input value="Submit" type="submit" />
        </form>
    '''

@route('/audio', method='POST')
def getaudio():
    name = request.forms.get('name')
    artist = request.forms.get('artist')
    lyrics = lyricwikia.get_lyrics(artist, name)
    tts = gTTS(text=lyrics, lang='en', slow=False)
    filename = str(random.randrange(999)) + '.mp3'
    tts.save(filename)
    return static_file(filename, root=filename, mimetype='audio/mpeg')
    os.remove(filename)

def check_login(username, password):
    if(username=="username" and password=="password"):
        return True
    else:
        return False


run(host='localhost', port=8080, debug=True)
