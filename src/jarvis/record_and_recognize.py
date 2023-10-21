# Citation complete
import pyaudio
import wave
import datetime

import os

from jarvis import autostop

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
THRESHOLD = bytes(180)

CWD = os.getcwd()
MEDIADIR = f"{CWD}/src/jarvis/recorded_speech_files"


def generate_file_name():
    f_name = str(datetime.datetime.now()) + ".wav"
    return f"{MEDIADIR}/{f_name}"


SPEECH_FILE = generate_file_name()


def record():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Start recording...")

    frames = []
    time = 3
    for i in range(0, int(RATE / CHUNK * time)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("recording stopped")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(SPEECH_FILE, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()
# Copied from tutorial: https://realpython.com/playing-and-recording-sound-python/#pyaudio
# Last accessed: Nov 12 2022


def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data
# Copied from tutorial: https://www.assemblyai.com/blog/python-speech-recognition-in-30-lines-of-code/
# Last accessed: # Last accessed Feb 4th, 2023

from deepgram import Deepgram
import json

DEEPGRAM_API_KEY = "df013c5e914d09190f34c752b03bc0b7f447b65b"

def recognize(path_to_file):
    # Initializes the Deepgram SDK
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    # Open the audio file
    with open(path_to_file, 'rb') as audio:
        # ...or replace mimetype as appropriate
        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        response = deepgram.transcription.sync_prerecorded(source, {'punctuate': False})
        print(json.dumps(response, indent=4))
        transcript = {"text": response["results"]["channels"][0]["alternatives"][0]["transcript"]}

    return transcript


# source: https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio
# Last accessed Oct 21, 2023

def record_and_recognize():
    autostop.record_to_file(SPEECH_FILE)
    return recognize(SPEECH_FILE)


if __name__ == "__main__":
    print(record_and_recognize())
