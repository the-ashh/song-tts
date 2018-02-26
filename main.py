from bottle import route, request, static_file, get, run
import lyricwikia
from gtts import gTTS
import os

@route('/')
def main():
    return static_file("index.html", root="./")

@get("/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./")

@route('/getlyric', method='POST')
def getaudio():
    name = request.forms.get('name')
    artist = request.forms.get('artist')
    filename = (name + "_" + artist + ".mp3").lower()
    if os.path.isfile('./audio/' + filename) == True:
        return '''<meta http-equiv="refresh" content="0; url=/audio/''' + filename + '''" />'''
    else:
        lyrics = lyricwikia.get_lyrics(artist, name)
        tts = gTTS(text=lyrics, lang='en', slow=False)
        tts.save("./audio/" + filename)
        return '''<meta http-equiv="refresh" content="0; url=/audio/''' + filename + '''" />'''

@get("/audio/<filepath:re:.*\.mp3>")
def giveaudio(filepath):
    return static_file(filepath, root="audio/")

run(host='localhost', port=8080, debug=True)
