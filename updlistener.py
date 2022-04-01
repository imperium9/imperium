import socket
import webbrowser

bind_ip = "127.0.0.1"
bind_port = 9998
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((bind_ip, bind_port))

print("[*] Ready for data at %s:%d" % (bind_ip, bind_port))

while True:
    data, addr = server.recvfrom(1024)

    print("[*] Got data from %s:%d: %s" % (addr[0], addr[1], data))
    if data==b'hacking nasa':
        webbrowser.open(url) 
    server.sendto(b"ACK!", addr)