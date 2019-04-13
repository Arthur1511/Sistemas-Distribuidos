import rpyc

connection = rpyc.connect('localhost', 18812)

print(connection.root.encrypt('Arthur Bernardo'))
