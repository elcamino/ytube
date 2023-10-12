#!/usr/bin/env python3

import argparse
import openai
from pytube import YouTube

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
    # Extract filename and replace extension with .txt
    txt_file_path = os.path.splitext(file_path)[0] + '.txt'
    # Write transcript to file
    with open(txt_file_path, 'w') as f:
        f.write(transcript)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download and transcribe audio from YouTube video.')
    parser.add_argument('--url', type=str, help='URL of the YouTube video')
    args = parser.parse_args()
    download_audio(args.url)
