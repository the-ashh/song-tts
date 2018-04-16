from bottle import route, request, static_file, get, run
import lyricwikia
from gtts import gTTS
import os
import json


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
    filename = ((name + "_" + artist + ".mp3").lower()).replace(" ", "")
    if not(os.path.isfile('./audio/' + filename)):
        lyrics = lyricwikia.get_lyrics(artist, name)
        tts = gTTS(text=lyrics, lang='en', slow=False)
        tts.save("./audio/" + filename)
    return ('''<meta http-equiv="refresh" content="0; url=/audio/''' +
            filename + '''" />''')

@route('/assistant', method='POST')
def assistant():
    data = request.json
    obj = json.load(data)
    artist = obj["inputs"][0]["rawInputs"][0]["query"]
    return(artist)


@get("/audio/<filepath:re:.*\.mp3>")
def giveaudio(filepath):
    return static_file(filepath, root="audio/")


run(host='localhost', port=8080, debug=True)
