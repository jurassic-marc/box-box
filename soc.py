import socket

# UDP_IP = "192.168.0.112" # PC
# UDP_IP = "172.23.52.255" # WSL via PC - port forwarding did not work
UDP_IP = "192.168.0.154" # Unix

UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def main():
    while True:
        data, addr = sock.recvfrom(2048) # buffer size is 1024 bytes
        print("received message: %s" % data)