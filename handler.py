import tkinter as tk
from crypt import crypt_message
from codigo_de_linha import pst, inverse_pst
from bin import str_to_bin, bin_to_string
from client import client
from server import server


def data_pipeline(message, frame):
    for widget in frame.winfo_children():
        widget.destroy()
    encrypted_message = crypt_message(message)
    bin_str = str_to_bin(encrypted_message)
    pst_message_list = pst([int(i) for i in bin_str])
    pst_message_str = "".join([f"{str(i)} " for i in pst_message_list])
    label_list = [
        tk.Label(master=frame, text=f"mensagem original: {message}"),
        tk.Label(master=frame, text=f"mensagem criptografada: {encrypted_message}"),
        tk.Label(master=frame, text=f"mensagem pseudoternaria: {pst_message_str}"),
    ]
    for label in label_list:
        label.pack()

    send_button = tk.Button(
        master=frame,
        text="enviar",
        width=50,
        command=lambda: client(pst_message_str.encode()),
    )
    send_button.pack()


def client_view(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    message_entry = tk.Entry(master=frame)
    message_entry.pack()
    continue_button = tk.Button(
        master=frame,
        text="continuar",
        width=50,
        command=lambda: data_pipeline(message_entry.get(), frame),
    )
    continue_button.pack()


# def server_view(frame):
# frame.destroy()
#
# pst_message_str = server()
# pst_message_list = [int(i) for i in pst_message_str]
# bin_str = inverse_pst(pst_message_list)
# encrypted_message = bin_to_string(bin_str)
# decrypted_message = crypt_message(encrypted_message)
# print(decrypted_message)


def main():
    window = tk.Tk()
    frame = tk.Frame(master=window, width=100, height=100)
    frame.pack()
    server_button = tk.Button(
        master=frame, text="server", width=50, command=lambda: server(frame)
    )
    client_button = tk.Button(
        master=frame, text="client", width=50, command=lambda: client_view(frame)
    )
    server_button.pack()
    client_button.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
