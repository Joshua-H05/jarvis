import sr_test

print("Enter CTRL+C to end recording...")
sr_test.stream.start_stream()

try:
    recognize_thread = sr_test.Thread(target=sr_test.recognize_using_weboscket, args=())
    recognize_thread.start()
    print(sr_test.MyRecognizeCallback.on_transcription())

    while True:
        pass
except KeyboardInterrupt:
    # stop recording
    sr_test.stream.stop_stream()
    sr_test.stream.close()
    sr_test.audio.terminate()
    sr_test.audio_source.completed_recording()