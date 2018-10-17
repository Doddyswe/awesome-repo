#A small example from the Python cryptography package

from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b'Encrypted secret message')
token
f.decrypt(token)
