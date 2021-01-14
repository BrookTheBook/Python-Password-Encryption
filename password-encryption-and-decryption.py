from cryptography.fernet import Fernet
key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b'Password')   #required to be bytes
print(ciphered_text)

unciphered_text = (cipher_suite.decrypt(ciphered_text))
print(unciphered_text)
