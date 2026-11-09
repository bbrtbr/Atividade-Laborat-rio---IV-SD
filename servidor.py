import socket
import threading
import time

s Visualizacao = {}

def checar_status():
    while True:
        time.sleep(2)
        agora = time.time()
        for worker_id, ultimo_ping in list(Visualizacao.items()):
            if agora - ultimo_ping > 8:
                print(f"[ALERTA] O Nó {worker_id} está OFFLINE!")
                del Visualizacao[worker_id]

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(('localhost', 5000))

t = threading.Thread(target=checar_status, daemon=True)
t.start()

print("Servidor Monitor rodando...")

while True:
    data, addr = servidor.recvfrom(1024)
    msg = data.decode('utf-8')
    if msg.startswith("PING:"):
        worker_id = msg.split(":")[1]
        Visualizacao[worker_id] = time.time()
        print(f"Heartbeat recebido de {worker_id}")