def encriptar(msg : bytearray) -> bytearray:
    largo = len(msg)
    msg1 = bytearray(b"")
    msg2 = bytearray(b"")
    msg3 = bytearray(b"")
    for i in range(3):
        for j in range(i, largo, 3):
            if i == 0:
                msg1.extend(msg[j:j + 1])
            elif i == 1:
                msg2.extend(msg[j:j + 1])
            elif i == 2:
                msg3.extend(msg[j:j + 1])
    msg1_primero = msg1[0]
    msg3_ultimo = msg3[-1]
    msg2_centrales = 0
    for k in range(1, len(msg2) - 1):
        msg2_centrales += msg2[k]
    suma = msg1_primero + msg2_centrales + msg3_ultimo
    if suma % 2 == 0:
        n = b"\x00"
        mensaje = n + msg3 + msg1 + msg2
    else:
        n = b"\x01"
        mensaje = n + msg1 + msg3 + msg2
    return bytearray(mensaje)


def desencriptar(msg : bytearray) -> bytearray:
    n = msg[0]
    msg = msg[1:]
    largo = len(msg)
    entero = largo // 3
    resto = largo % 3    
    if resto == 0 and n == 0:
        a, b, c = msg[entero: 2 * entero], msg[2 * entero:], msg[:entero]
    elif resto == 1 and n == 0:
        a, b, c = msg[entero: 2 * entero + 1], msg[2 * entero + 1:], msg[:entero]
    elif resto == 2 and n == 0:
        a, b, c = msg[entero: (2 * entero) + 1], msg[(2 * entero) + 1:], msg[:entero]
    elif resto == 0 and n == 1:
        a, b, c = msg[:entero], msg[2 * entero:], msg[entero: 2 * entero]
    elif resto == 1 and n == 1:
        a, b, c = msg[:entero + 1], msg[(2 * entero) + 1:], msg[entero + 1: (2 * entero) + 1]
    elif resto == 2 and n == 1:
        a, b, c = msg[:entero + 1], msg[(2 * entero) + 1:], msg[entero + 1: (2 * entero) + 1]
    mensaje = b""
    for i in range(entero):
        mensaje += a[i:i + 1]
        mensaje += b[i:i + 1]
        mensaje += c[i:i + 1]
    if resto == 1:
        mensaje += a[len(a) - 1:]
    elif resto == 2:
        mensaje += a[len(a) - 1:]
        mensaje += b[len(b) - 1:]
    return bytearray(mensaje)


if __name__ == "__main__":
    # Testear encriptar
    msg_original = bytearray(b'\x05\x08\x03\x02\x04\x03\x05\x09\x05\x09\x01')
    msg_esperado = bytearray(b'\x01\x05\x02\x05\x09\x03\x03\x05\x08\x04\x09\x01')
    msg_encriptado = encriptar(msg_original)
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")
    
    # Testear desencriptar
    msg_desencriptado = desencriptar(msg_esperado)
    if msg_desencriptado != msg_original:
        print("[ERROR] Mensaje descencriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")
