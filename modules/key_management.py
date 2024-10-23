from Crypto.Cipher import AES
class KeyManagement:
    def __init__(self, aes_key):
        self.aes_key = aes_key
    def encrypt(self, private_key):
        cipher=AES.new(self.aes_key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(private_key.encode())
        # Log the values
        print(f"Encryption - Nonce: {nonce}, Tag: {tag}, Ciphertext: {ciphertext}")
        return nonce, ciphertext, tag
    def decrypt_key(self, nonce, ciphertext, tag):
        cipher = AES.new(self.aes_key, AES.MODE_EAX, nonce=nonce)
    
        #Log the values before decryption
        print(f"Decryption - Nonce: {nonce}, Tag: {tag}, Ciphertext: {ciphertext}")
    
        try:
            private_key = cipher.decrypt_and_verify(ciphertext, tag)
            return private_key.decode()  # Make sure the original data is valid UTF-8 encoded text
        except ValueError:
            print("Decryption failed: MAC check failed")
            raise
