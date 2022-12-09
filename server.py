import socket
import tkinter as tk

from bin import bin_to_string
from codigo_de_linha import inverse_pst, pst
from crypt import crypt_message

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


def server(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                pst_message_list = [int(i) for i in data.decode()[:-1].split(" ")]
                bin_str = inverse_pst(pst_message_list)
                pst(bin_str)
                encrypted_message = bin_to_string(bin_str)
                decrypted_message = crypt_message(encrypted_message)

                label_list = [
                    tk.Label(
                        master=frame, text=f"mensagem original: {decrypted_message}"
                    ),
                    tk.Label(
                        master=frame,
                        text=f"mensagem criptografada: {encrypted_message}",
                    ),
                    tk.Label(
                        master=frame,
                        text=f"mensagem pseudoternaria: {pst_message_list}",
                    ),
                ]
                for label in label_list:
                    label.pack()


if __name__ == "__main__":
    server()
