import pyaudio
import wave
import datetime
from google.oauth2 import service_account
from google.cloud import speech
import streamlit as st

from jarvis import autostop

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
THRESHOLD = bytes(180)


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
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["google_key"])
    client = speech.SpeechClient(credentials=credentials)

    with open(file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        enable_word_confidence=True,
    )

    response = client.recognize(config=config, audio=audio)

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        results = {
                "text":format(alternative.transcript),
                "confidence": alternative.words[0].confidence,
                }
        return results


# source https://learndataanalysis.org/source-code-getting-started-with-google-cloud-speech-to-text-api-in-python/


def record_and_recognize():
    autostop.record_to_file(SPEECH_FILE)
    return recognize(SPEECH_FILE)


if __name__ == "__main__":
    print(record_and_recognize())
