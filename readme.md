## Bruno e Marrone - client-server 

Esse repositório contém uma aplicação cliente e servidor que se propõe a implementar o seguinte desafio:

um projeto para um sistema doméstico composto de um servidor de mídia em separado, que leva em conta a ligação com um cliente sem
fio. Esse úlHmo está conectado a um equipamento (analógico) de áudio e vídeo e transforma as sequências de mídia digital em saída analógica. O servidor executa em uma máquina separada, possivelmente conectada à Internet, mas não há nenhum teclado nem monitor conectado a ela.

## funcionamento
Ao inicializar o servidor, ele irá aguardar por uma conexão de um cliente. O cliente, por sua vez, irá se conectar ao servidor e enviar um arquivo de mídia (vídeo ou áudio) para que o servidor possa transmitir tal arquivo para um equipamento de áudio e vídeo.


## Video Demo
<video width="320" height="240" controls>
  <source src="demo/0202.mov" type="video/mp4">
</video>