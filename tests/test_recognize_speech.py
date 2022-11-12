import jarvis.recognise_speech as jrs


def test_recognise_hello():
    assert isinstance(jrs.recognise("Hello"), Speech)


def test_respond_to_hello():
    speech = Speech("Hello")
    assert jrs.respond(speech) is None
