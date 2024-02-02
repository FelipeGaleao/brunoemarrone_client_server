# client.py

import socket
import os

def receive_media(connection, media_file):
    with open(media_file, 'wb') as file:
        data = connection.recv(1024)
        while data:
            file.write(data)
            data = connection.recv(1024)

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print("Conectando ao servidor...")
    client_socket.connect(('127.0.0.1', 5001))
    print("Conexão estabelecida!")
    
    # ask for media_file
    media_file_request = input("Digite o nome do arquivo de mídia: ")
    musicas = ['brunoemarrone_agarradaemmim.mp3', 'brunoemarrone_agora.mp3']
    if media_file_request in musicas:
        media_file = media_file_request.encode()
    else:
        print("Arquivo de mídia não encontrado!")
        return

    # send media_file
    client_socket.send(media_file)

    print("Recebendo arquivo de mídia...")

    os.system('mkdir download')

    # receive media_file
    media_file = 'download/brunoemarrone_agarradaemmim.mp3'
    receive_media(client_socket, media_file)

    os.system(f'afplay {media_file}')

    client_socket.close()

if __name__ == "__main__":
    start_client()
