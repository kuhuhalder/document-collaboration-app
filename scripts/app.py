# # from flask import Flask, render_template
# # from flask_socketio import SocketIO, emit

# # app = Flask(__name__)
# # socketio = SocketIO(app)

# # document = "This is a test document."

# # @app.route('/')
# # def index():
# #     return render_template('index.html', document=document)

# # @socketio.on('connect')
# # def handle_connect():
# #     emit('document', document)

# # @socketio.on('edit')
# # def handle_edit(data):
# #     global document
# #     document = data['text']
# #     emit('document', document, broadcast=True)

# # if __name__ == '__main__':
# #     socketio.run(app)


# # from flask import Flask, render_template
# # from flask_socketio import SocketIO, emit

# # app = Flask(__name__)
# # socketio = SocketIO(app)

# # @app.route('/')
# # def index():
# #     return render_template('index1.html')

# # @socketio.on('update')
# # def handle_update(json):
# #     emit('update', json, broadcast=True)

# # if __name__ == '__main__':
# #     socketio.run(app, debug=True)

# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# socketio = SocketIO(app)

# @app.route('/')
# def index():
#     return render_template('index2.html')

# @socketio.on('connect')
# def handle_connect():
#     emit('document_contents', 'Hello, world!')

# @socketio.on('document_update')
# def handle_document_update(new_contents):
#     emit('document_update', new_contents, broadcast=True)


# if __name__ == '__main__':
#     socketio.run(app, debug=True)