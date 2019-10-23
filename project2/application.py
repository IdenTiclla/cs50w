import os
from flask_socketio import SocketIO, emit, send, join_room
from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels_list = []
messages = {}
users = []


@app.route("/")
def index():
    return render_template("index.html", async_mode=socketio.async_mode)


@socketio.on("connect")
def connect():
    print("new user connected")

@socketio.on("disconnect")
def disconnect():
    print("user was diconnected")
    
@socketio.on('if channels')
def channels():
    if channels_list:
        socketio.emit("if channels", {"channels": channels_list}, broadcast=True)



# execute when a message is send
@socketio.on("sending message")
def messageHandler(data):
    # add data to the messages of the channel in question
    messages[data["channel"]].append(data)
    # store only the 100 most recent messages per channel
    if len(messages[data["channel"]]) > 100:
    	messages[data["channel"]].pop(0)
    channel = data["channel"]
    msgs = messages[data["channel"]]
    data = {"channel":channel, "messages":msgs}
    # send back the time, the message and the username to the client side
    emit("receiving messages",data, broadcast=True)



@socketio.on("channel_creation")
def channel_creation(channel):
    # channel name is taken
    if channel in channels_list:
        emit("channel_error",{"error":"This name is already taken!"})
    #success
    else:
        # add channel to the list of channels
        channels_list.append(channel)
        messages[channel] = []
        # add user to the channel
        join_room(channel)
        current_channel = channel
        emit("join_channel", {"channel": channel})
    
# this event is executed when the user login in a channel
@socketio.on("join_channel")
def join_channel(data):
    channel = data["channel"]
    # if username not in list of users
    username = data["username"]
    if username not in users:
        users.append(username)
    if channel not in channels_list:
        channels_list.append(channel)
        # add user to the channel
        join_room(data["channel"])
    emit("join_channel", {"channel": channel})
    emit("receiving messages", {"channel":channel, "messages":messages[data["channel"]]})

@socketio.on('delete message')
def delete_message(data):
    channel = data["channel"]
    messages[channel].remove(data)
    emit("receiving messages", {"channel":channel, "messages":messages[data["channel"]]},broadcast=True)

if __name__ == "__main__":    
    socketio.run(app, port=8000)