from bottle import Bottle, route, request, static_file, get, run
import lyricwikia
from gtts import gTTS
from tempfile import TemporaryFile
import random
import os

filename = "mada.mp3"

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

@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="css")

@route('/')
def audio():
    return '''
        <form action="/audio/''' + filename + '''"method="post">
            Song Name: <input name="name" type="text" />
            Song Artist: <input name="artist" type="text" />
            <input value="Submit" type="submit" />
        </form>
    '''

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/path/to/your/static/files')

@route('/audio/mada.mp3', method='POST')
def getaudio(filepath):
    name = request.forms.get('name')
    artist = request.forms.get('artist')
    lyrics = lyricwikia.get_lyrics(artist, name)
    tts = gTTS(text=lyrics, lang='en', slow=False)
    tts.save('./audio/'+filename)
    return static_file(filepath, root='./audio/'+filename, mimetype='audio/mpeg')
    os.remove('./audio/'+filename)
'''
def check_login(username, password):
    if(username=="username" and password=="password"):
        return True
    else:
        return False
'''

run(host='localhost', port=8080, debug=True)
