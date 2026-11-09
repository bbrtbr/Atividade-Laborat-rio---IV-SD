import socket
import time
import sys

if len(sys.argv) > 1:
    worker_id = sys.argv[1]
else:
    worker_id = "Worker_1"

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Iniciando {worker_id}...")

while True:
    msg = f"PING:{worker_id}"
    cliente.sendto(msg.encode('utf-8'), ('localhost', 5000))
    time.sleep(3)
