import time
import socket

server = "irc.chat.twitch.tv"
port = 6667
channel = input("Enter your channel name: ")
channel2 = input("Enter another channel name: ")
oauth = ''

with open("oauth.txt", "r") as file:
        oauth = file.read()
nickname = f"bot_1"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))

print(f"[{time.strftime('%X')}] Connecting to {channel}")
irc.send(f"PASS {oauth}\n".encode("utf-8"))
irc.send(f"NICK {nickname}\n".encode("utf-8"))
irc.send(f"JOIN #{channel}\n".encode("utf-8"))

print(f"[{time.strftime('%X')}] Connecting to {channel2}")
irc.send(f"JOIN #{channel2}\n".encode("utf-8"))

while True:
    try:
        resp = irc.recv(2048).decode("utf-8")
        if resp.startswith("PING"):
            irc.send("PONG\n".encode("utf-8"))
        elif len(resp) > 0:
            username = resp.split(' ')[0].split('!')[0][1:]
            message = resp.split(':')[-1].strip()

            print(f"[{time.strftime('%X')}] {username}: {message}")
    except Exception as e:
        print(f"[{time.strftime('%X')}] Error: {e}")
        break

    try:
        resp2 = irc.recv(2048).decode("utf-8")
        if resp2.startswith("PING"):
            irc.send("PONG\n".encode("utf-8"))
        elif len(resp2) > 0:
            username2 = resp2.split(' ')[0].split('!')[0][1:]
            message2 = resp2.split(':')[-1].strip()

            print(f"[{time.strftime('%X')}] {username2}: {message2}")
    except Exception as e:
        print(f"[{time.strftime('%X')}] Error: {e}")
        break

irc.close()
