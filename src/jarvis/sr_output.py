import sr_test
import time

sr_test.generate_file_name()
print("Enter CTRL+C to end recording...")
sr_test.stream.start_stream()


recognize_thread = sr_test.Thread(target=sr_test.ecognize_using_weboscket, args=())
recognize_thread.start()
time.sleep(5)
sr_test.stream.close()

