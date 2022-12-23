from jarvis import parse, speak


def record():
    pass


def sr():
    """ Recognize recording& return string"""
    pass


def recog_recording():
    return sr(record())


def ask_parse_execute():
    speak.greet()
    speak.ask_func_type()
    recog_recording()

