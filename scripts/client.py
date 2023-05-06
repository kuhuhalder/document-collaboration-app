# import threading
# import socketio
# import random

# sio = socketio.Client()

# def connect():
#     sio.connect('http://127.0.0.1:5000')

# def edit():
#     while True:
#         sio.emit('edit', {'text': 'This is a test edit by client ' + str(threading.current_thread().name)})

# def run():
#     connect()
#     edit()

# if __name__ == '__main__':
#     for i in range(10):
#         t = threading.Thread(target=run)
#         t.start()

import time
import random
import string
import socketio

sio = socketio.Client()

def generate_text(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('update')
def on_text_update(text):
    print(f'Received text update: {text}')
    
    
if __name__ == '__main__':
    for i in range(5):
        sio.connect('http://localhost:5000')
        print(f'User {i} connected to server')
        time.sleep(1)

        for j in range(5):
            text = generate_text(10)
            sio.emit('text', text)
            print(f'User {i} sent text: {text}')
            time.sleep(1)

        sio.disconnect()
        print(f'User {i} disconnected from server')

