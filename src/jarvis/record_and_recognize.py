import pyaudio
import wave
import datetime
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from secret import auth_key, link

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
    url = link

    authenticator = IAMAuthenticator(api_key)
    stt = SpeechToTextV1(authenticator=authenticator)
    stt.set_service_url(url)

    with open(file, "rb") as f:
        r = stt.recognize(audio=f, content_type="audio/wav", model="en-US_NarrowbandModel").get_result()
        text = r["results"][0]["alternatives"][0]["transcript"]
        confidence = r["results"][0]["alternatives"][0]["confidence"]
        return text, confidence


def record_and_recognize():
    record()
    return recognize(SPEECH_FILE)


if __name__ == "__main__":
    print(record_and_recognize())
