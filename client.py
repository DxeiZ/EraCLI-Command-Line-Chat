import socket
from colorama import Fore, Back, Style
import signal
import sys

server = socket.socket()

serverhost = input(str(Fore.MAGENTA+'Ana bilgisayar adını veya ana bilgisayar IP\'sini girin: '+Fore.RESET))
port = 8080
server.connect((serverhost, port))
servername = serverhost.capitalize()

host = socket.gethostname()
username = host.capitalize()

print(Fore.GREEN+'Sohbet sunucusuna bağlandı'+Fore.RESET)

while True:
    try:
        incoming_message = server.recv(1024)
        incoming_message = incoming_message.decode()
        print(Fore.RED + servername + ': ' + incoming_message + Fore.RESET)
        message = input(str(Fore.CYAN+'[Sen] > '+Fore.RESET))
        message = message.encode()
        server.send(message)
        if message.decode() == "exit":
            break
    except:
        print(Fore.YELLOW+"Bağlantı hatası. Program kapatılıyor."+Fore.RESET)
        server.close()
        sys.exit(0)


def signal_handler(sig, frame):
    print(Fore.YELLOW+'\nProgram sonlandırılıyor...'+Fore.RESET)
    server.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
