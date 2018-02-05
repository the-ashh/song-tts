from bottle import route, request, static_file, get, run
import lyricwikia
from gtts import gTTS
import random
import os

filename = str(random.randrange(999)) + ".mp3"


@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="css")


@route('/')
def main():
    return '''
        <form action="/getlyric "method="post">
            Song Name: <input name="name" type="text" />
            Song Artist: <input name="artist" type="text" />
            <input value="Submit" type="submit" />
        </form>
    '''.format(filename)


@route('/getlyric', method='POST')
def getaudio():
    name = request.forms.get('name')
    artist = request.forms.get('artist')
    lyrics = lyricwikia.get_lyrics(artist, name)
    tts = gTTS(text=lyrics, lang='en', slow=False)
    tts.save('./audio/' + filename)
    return static_file('./audio/' + filename, root='./audio/' + filename, mimetype='audio/mpeg')


run(host='localhost', port=8080, debug=True)
