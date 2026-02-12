import hashlib

x = input("podaj tekst  ")
i = hashlib.sha256(x.encode('utf-8'))
print(i.hexdigest())