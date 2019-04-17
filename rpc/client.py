import rpyc

connection = rpyc.connect('localhost', 18812)

print("Trabalho de Sistemas Distribuídos – Professora Carla Lara.\n")
print("\t\t\t MENU")
print("\t 1 - CRIPTOGRAFAR")
print("\t 2 - DESCRIPTOGRAFAR\n")
op = int(input("Escolha a opção desejada:"))

if op == 1:
    msg = input("Digite a mensagem a ser criptografada:")
    print(connection.root.encrypt(msg))

if op == 2:
    msg = input("Digite a mensagem a ser descriptografada:")
    print(connection.root.encrypt(msg))
