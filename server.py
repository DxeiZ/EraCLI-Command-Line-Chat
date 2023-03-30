import socket
import signal
import sys
from colorama import Fore, Back, Style

server = socket.socket()

host = socket.gethostname()
username = host.capitalize()
print(Fore.MAGENTA + 'Host adresiniz:', Style.BRIGHT + Back.MAGENTA + Fore.WHITE + host + Style.RESET_ALL)

port = 8080
server.bind((host, port))
print(Fore.LIGHTYELLOW_EX + 'Bağlantı için bekleniliyor..' + Style.RESET_ALL)

server.listen(5)  # 5 bağlantı kabul edilebilir
print(Fore.GREEN + 'Bağlantılar kabul edilebilir..' + Style.RESET_ALL)

conn, addr = server.accept()
print(Fore.GREEN + str(addr[0]), Fore.RESET + ':', Fore.GREEN + str(addr[1]), Fore.LIGHTGREEN_EX + ' sunucuya bağlandı\n' + Style.RESET_ALL)

while True:
    message = input(Fore.YELLOW + '[Sen] > ' + Fore.RESET)
    message = message.encode()
    conn.send(message)

    while True:
        incoming_message = conn.recv(1024).decode()
        if not incoming_message:
            break
        print(Fore.CYAN + '[' + str(addr[0]) + '] : ' + incoming_message + Style.RESET_ALL)

        message = input(Fore.YELLOW + '[Sen] > ' + Fore.RESET)
        message = message.encode()
        conn.send(message)

    conn.close()
    print(Fore.RED + 'Bağlantı kesildi.. Bekleniyor..' + Style.RESET_ALL)
    conn, addr = server.accept()
    print(Fore.GREEN + str(addr[0]), Fore.RESET + ':', Fore.GREEN + str(addr[1]), Fore.LIGHTGREEN_EX + ' sunucuya bağlandı\n' + Style.RESET_ALL)


def signal_handler(sig, frame):
    print('Program sonlandırılıyor...')
    server.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
