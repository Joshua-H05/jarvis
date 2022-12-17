import websockets
import asyncio
import base64
import json
from secret import auth_key
import pyaudio
import datetime
import streamlit as st
from jarvis import speak

if "run" not in st.session_state:
    st.session_state["run"] = False

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()

# starts recording
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

# the AssemblyAI endpoint we're going to hit
URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"


def start_session():
    st.session_state["run"] = True


def end_session():
    st.session_state["run"] = False


st.title("Your personal AI assistant")
start, stop = st.columns(2)
start.button("Start Session", on_click=start_session)
stop.button("End Session", on_click=end_session)


def generate_file_name():
    f_name = str(datetime.datetime.now())
    return f_name


SPEECH_FILE = generate_file_name()


def save_to_file(info):
    with open(SPEECH_FILE, "a") as f:
        f.write(f"{info}\n")
        f.flush()


async def send_receive():
    print(f'Connecting websocket to url ${URL}')

    async with websockets.connect(
            URL,
            extra_headers=(("Authorization", auth_key),),
            ping_interval=5,
            ping_timeout=20
    ) as _ws:

        await asyncio.sleep(0.1)
        print("Receiving SessionBegins ...")
        session_begins = await _ws.recv()
        print(session_begins)
        print("Sending messages ...")

        async def send():
            greet = True
            while st.session_state["run"]:
                try:
                    if greet:
                        speak.greet()
                        greet = False
                    data = stream.read(FRAMES_PER_BUFFER, exception_on_overflow=False)
                    data = base64.b64encode(data).decode("utf-8")
                    json_data = json.dumps({"audio_data": str(data)})
                    await _ws.send(json_data)

                except websockets.exceptions.ConnectionClosedError as e:
                    print(e)
                    assert e.code == 4008
                    break

                except Exception as e:
                    assert False, "Not a websocket 4008 error"

                await asyncio.sleep(0.01)

            return True

        async def receive():
            while st.session_state["run"]:
                try:
                    result_str = await _ws.recv()
                    result = json.loads(result_str)
                    if result["message_type"] == "FinalTranscript":
                        text = result['text']
                        st.markdown(text)
                        confidence = result["confidence"]
                        time = result["created"]
                        info = {"text": text, "confidence": confidence, "time registered": time}
                        print(f" You:{text}")
                        save_to_file(info)

                except websockets.exceptions.ConnectionClosedError as e:
                    print(e)
                    assert e.code == 4008
                    break

                except Exception as e:
                    assert False, "Not a websocket 4008 error"

        send_result, receive_result = await asyncio.gather(send(), receive())
        print(receive_result)

asyncio.run(send_receive())
