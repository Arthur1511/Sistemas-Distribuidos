from rpyc import Service
from rpyc.utils.server import ThreadedServer


alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


class Criptografia(Service):

    def exposed_encrypt(self, text):
        plain = list(text)
        encrypted = "Encryped text: "
        for i in range(len(plain)):
            for j in range(len(alph)):
                # print i, j
                if plain[i] == alph[j]:
                    if j < len(alph) - 3:
                        toenc = alph[j + 3]
                    elif j == len(alph) - 3:
                        toenc = alph[0]
                    elif j == len(alph) - 2:
                        toenc = alph[1]
                    elif j == len(alph) - 1:
                        toenc = alph[2]
                    else:
                        print("DEBUG: nichts true")
                    encrypted += toenc
            if plain[i] == " ":
                encrypted += " "

        print("Trabalho de Sistemas Distribuídos – Professora Carla Lara.")

        return encrypted

    def exposed_decrypt(self, text):
        encrypted = list(text)
        decrypted = "Decrypted text: "
        for i in range(len(encrypted)):
            for j in range(len(alph)):
                # print i, j
                if encrypted[i] == alph[j]:
                    if j < len(alph) - 3:
                        todec = alph[j - 3]
                    elif j == 2:
                        todec = alph[len(alph) - 3]
                    elif j == 1:
                        todec = alph[len(alph) - 2]
                    elif j == 0:
                        todec = alph[len(alph)]
                    else:
                        print("DEBUG: nichts true")
                    decrypted += todec
            if encrypted[i] == " ":
                decrypted += " "

        print("Trabalho de Sistemas Distribuídos – Professora Carla Lara.")

        return decrypted


if __name__ == '__main__':
    s = ThreadedServer(Criptografia, port=18812)
    s.start()