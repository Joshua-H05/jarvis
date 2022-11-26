import jarvis.recognise_speech as jrs


def test_recognise_hello():
    assert isinstance(jrs.recognise(), jrs.Speech)


def test_respond_to_hello():
    speech = jrs.Speech("Hello")
    assert jrs.Speech.respond(speech) is None
