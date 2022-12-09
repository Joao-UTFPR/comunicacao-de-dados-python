def crypt_message(message):
    encrypted_message = ""
    for i in range(len(message)):
        encrypted_message += message[len(message) - i - 1]
    return encrypted_message
