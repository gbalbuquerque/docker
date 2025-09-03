import zmq
from time import sleep

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://broker:5555")

i = 0
while True:
    print(f"Mensagem {i}:", end=" ", flush=True)
    socket.send(b"Hello")
    mensagem = socket.recv()
    print(f"{mensagem}", flush=True)
    i += 1
    sleep(0.5)
