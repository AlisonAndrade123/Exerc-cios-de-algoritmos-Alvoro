from cryptography.fernet import Fernet

chave = Fernet.generate_key()
fernet = Fernet(chave)

mensagem = input("Digite uma mensagem para criptografar: ").encode()

mensagem_criptografada = fernet.encrypt(mensagem)
print("Mensagem criptografada:", mensagem_criptografada.decode())

mensagem_descriptografada = fernet.decrypt(mensagem_criptografada).decode()
print("Mensagem descriptografada:", mensagem_descriptografada)