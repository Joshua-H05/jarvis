import pyaudio
import wave
import datetime
import requests
from secret import auth_key


UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
TRANSCRIPTION_ENDPOINT = "https://api.assemblyai.com/v2/transcript"

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


def generate_file_name():
    f_name = str(datetime.datetime.now()) + ".wav"
    return f_name


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


def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


def recognize(file):
    api_key = auth_key
    headers = {"authorization": api_key, "content-type": "application/json"}
    upload_response = requests.post(UPLOAD_ENDPOINT, headers=headers, data=read_file(file))
    audio_url = upload_response.json()["upload_url"]
    transcript_request = {'audio_url': audio_url}
    transcript_response = requests.post(TRANSCRIPTION_ENDPOINT, json=transcript_request, headers=headers)
    _id = transcript_response.json()["id"]

    while True:
        polling_response = requests.get(TRANSCRIPTION_ENDPOINT + "/" + _id, headers=headers)

        if polling_response.json()['status'] == 'completed':
            return polling_response.json()['text'], polling_response.json()["confidence"]
        elif polling_response.json()['status'] == 'error':
            raise Exception("Transcription failed. Make sure a valid API key has been used.")


def record_and_recognize():
    record()
    return recognize(SPEECH_FILE)

if __name__ == "__main__":
    record_and_recognize()