from bottle import route, request, static_file, get, run
import lyricwikia
from gtts import gTTS
import random
import os

filename = str(random.randrange(999)) + ".mp3"

@route('/')
def main():
    return '''
        <form action="/getlyric "method="post">
            Song Name: <input name="name" type="text" />
            Song Artist: <input name="artist" type="text" />
            <input value="Submit" type="submit" />
        </form>
    '''

@route('/getlyric', method='POST')
def getaudio():
    name = request.forms.get('name')
    artist = request.forms.get('artist')
    lyrics = lyricwikia.get_lyrics(artist, name)
    tts = gTTS(text=lyrics, lang='en', slow=False)
    tts.save('./audio/' + filename)
    return '''<meta http-equiv="refresh" content="0; url=/audio/'''+filename+'''" />'''

@get("/audio/<filepath:re:.*\.mp3>")
def giveaudio(filepath):
    return static_file(filepath, root="audio/")

'''@route('/{}'.format(path))
def giveaudio():
'''


run(host='localhost', port=8080, debug=True)
