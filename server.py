# Писал Ляпин Дмитрий, Б9122-01.03.02мкт

import socket
import tkinter as tk

def start_server():
    global lbl, ip, PORT
    port = 2000
    HOST = (ip, port)
    server = socket.create_server(HOST)
    server.listen(1)
    print('Start listening')

    client_socket, address = server.accept()
    print(f'New connection from {address}')
    while 1:
        data = client_socket.recv(1024).decode()
        if data == '1':
            lbl.config(text=str(int(lbl.cget("text")) + 1))
            print(f'now its {lbl.cget("text")}')
        else:
            print(f'Connection from {address} interruped!')
            break


window = tk.Tk()
COUNTER = str(0)
PORT = 2000
ip = socket.gethostbyname(socket.gethostname())

ip_lbl = tk.Label(window, text = f'Ваш сокет:\n{ip}:{PORT}', font=("Helvetica", "12"))
ip_lbl.pack()
lbl = tk.Label(window, text = COUNTER, font=("Helvetica", "16"))
lbl.pack()
button = tk.Button(window, text="Start Server", font=("Helvetica", "12"), command=start_server)
button.pack()

window.mainloop()
