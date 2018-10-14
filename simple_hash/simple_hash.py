import hashlib
sha3512 = hashlib.sha3_512()
sha3512.update(b'Hashed Pythonic Passphrase')
sha3512.digest()
