from mido.sockets import PortServer, connect
import mido

alesis = mido.get_output_names()[1]
port = mido.open_output(alesis)

# In Line 107 of:
# env/lib/python3.8/site-packages/mido/sockets.py,
# change if byte == '' to if byte == b''

with PortServer('0.0.0.0', 8080) as server:
    clients = []
    while True:
        # Handle connections.
        client = server.accept(block=False)
        if client:
            print('Connection from {}'.format(client.name))
            clients.append(client)

        for i, client in enumerate(clients):
            if client.closed:
                print('{} disconnected'.format(client.name))
                del clients[i]

        # Receive messages.
        for client in clients:
            for message in client.iter_pending():
                print('Received {} from {}'.format(message, client))
                port.send(message)
