from flask import Flask
from markupsafe import escape
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
app = Flask(__name__)

@app.route('/app/<size>')
def rand_crypt(size):
    plaintext=get_random_bytes(int(size))
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(b'%s'%plaintext) 
    return f'{escape(ciphertext)}'