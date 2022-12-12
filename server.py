import socket
import tkinter as tk
import re
from math import ceil

from bin import bin_to_string
from codigo_de_linha import inverse_pst, pst
from crypt import crypt_message

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


def server(window):
    # for widget in frame.winfo_children():
    #     widget.destroy()
    window.destroy()
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
                conn.sendall(data)

                pst_message_list = [int(i) for i in data.decode()[:-1].split(" ")]
                pst_message_string = re.sub("(.{32})", "\\1\n", "".join([f"{str(i)} " for i in pst_message_list]), 0, re.DOTALL)
                bin_str = inverse_pst(pst_message_list)
                pst(bin_str)
                encrypted_message = bin_to_string(bin_str)
                decrypted_message = crypt_message(encrypted_message)

                window = tk.Tk()

                label_list = [
                    tk.Label(
                        master=window, text=f"mensagem original: {decrypted_message}"
                    ),
                    tk.Label(
                        master=window,
                        text=f"mensagem criptografada: {encrypted_message}",
                    ),
                    tk.Label(
                        master=window,
                        text=f"mensagem pseudoternaria: \n{pst_message_string}",
                    ),
                ]
                for label in label_list:
                    label.pack()


if __name__ == "__main__":
    server()
