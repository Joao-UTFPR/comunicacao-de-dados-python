from codigo_de_linha import pst, inverse_pst

def str_to_bin(str):
    return ' '.join(format(ord(x)+4, 'b') for x in str)

def bin_to_string(data):
    mensagem=""
    print(len(data))
    for i in range(int(len(data)/7)):
        # print(int("".join(str(x) for x in data[7*i:7*(i+1)]),2)-4)
        mensagem+=chr(int("".join(str(x) for x in data[7*i:7*(i+1)]),2)-4)
    return mensagem

def main():
    a = "oi tudo bem"
    b = str_to_bin(a)
    print(b)
    # b=a.encode()
    # print()
    data = [int(i) for i in b]
    print(len(data))

    # data_pseudoternaria=pst(data)
    # data_despseudoternaria=inverse_pst(data_pseudoternaria)
    # print(data)
    # print(data_pseudoternaria)
    # print(data_despseudoternaria)

    # print(bin_to_string(data_despseudoternaria))
    # print("".join(str(x) for x in data_despseudoternaria).decode(encoding="UTF-8"))


if __name__=="__main__":
    main()