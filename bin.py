def resize_bin(bin):
    if len(bin) == 8:
        return bin
    else:
        for i in range(8 - len(bin)):
            bin = "0" + bin
    return bin


def str_to_bin(str):
    return "".join(resize_bin(format(ord(x) + 4, "b")) for x in str)


def bin_to_string(data):
    mensagem = ""
    for i in range(int(len(data) / 8)):
        print("".join(str(x) for x in data[8 * i : 8 * (i + 1)]))
        mensagem += chr(int("".join(str(x) for x in data[8 * i : 8 * (i + 1)]), 2) - 4)
    return mensagem
