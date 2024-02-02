# server.py

import socket
import uuid
import os

def send_media(connection, media_file):
    with open(media_file, 'rb') as file:
        data = file.read(1024)
        while data:
            connection.send(data)
            data = file.read(1024)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5001))
    server_socket.listen(1)

    print("Aguardando conexão do cliente...")

    connection, address = server_socket.accept()
    print("Conexão estabelecida:", address)
     
    # receive media_file name
    media_file = connection.recv(1024).decode()
    if not media_file:
        print("Nome do arquivo de mídia não recebido!")
        return
    
    print("Arquivo de mídia recebido:", media_file)

    # send media_file
  
    new_name = str(uuid.uuid4()) + '.mp3'
    
    # copy media_file to new_name
    os.system(f'cp {media_file} {new_name}')

    # move to to_be_download
    if not os.path.exists('to_be_download'):
        os.system('mkdir to_be_download')

    os.system(f'mv {new_name} to_be_download/')

    media_file = new_name

    send_media(connection, f"to_be_download/{media_file}")
    print("Arquivo de mídia enviado!")
    
    # remove media_file
    os.system(f'rm to_be_download/{media_file}')

    connection.close()

if __name__ == "__main__":
    start_server()
