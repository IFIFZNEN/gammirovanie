mode = input('Viberite mode: [E]ncrypt ||| [D]ecrypt: ')

if mode == 'E':
    message = list(input("Vashe slovo: "))
    key = input("Vash kluch: ")
    for symbol in range(len(message)):
        try: message[symbol] = chr(ord(message[symbol]) ^ int(key))
        except ValueError: message[symbol] = chr(ord(message[symbol]) ^ ord(key))
    print("Vash zashifrovanniy text:","".join(message))
    with open("crypt.txt","w") as file:
        file.write("".join(message))
    print(message)


elif mode == 'D':
    message = list(input("Vash shifr: "))
    key = input("Vash kluch: ")
    for symbol in range(len(message)):
        try: message[symbol] = chr(ord(message[symbol]) ^ int(key))
        except ValueError: message[symbol] = chr(ord(message[symbol]) ^ ord(key))
    print("Vashe isxodnoe slovo:","".join(message))
