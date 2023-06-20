# find_open_port.py
import socket
from contextlib import closing

def find_open_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]

if __name__ == "__main__":
    open_port = find_open_port()
    print(f"Available port: {open_port}")