#!/usr/bin/env python3

from flask import Flask, request
import openai
from pytube import YouTube

app = Flask(__name__)

def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file)
    return response["text"]

def download_audio(url):
    import os
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    file_path = stream.download()
    transcript = transcribe_audio(file_path)
    return transcript

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        transcript = download_audio(url)
        return {"transcript": transcript}
    return '''
        <form method="POST" id="transcribeForm">
            YouTube URL: <input type="text" name="url">
            <input type="submit" value="Transcribe">
        </form>
        <div id="transcript"></div>
        <script>
            document.getElementById('transcribeForm').addEventListener('submit', function(event) {
                event.preventDefault();
                fetch('/', {
                    method: 'POST',
                    body: new FormData(this)
                }).then(response => response.json())
                .then(data => {
                    document.getElementById('transcript').textContent = data.transcript;
                });
            });
        </script>
    '''

if __name__ == "__main__":
    app.run(debug=True)
