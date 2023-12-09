

#CYBER_SECURITY_PROJECT
#PROJECT_NAME : Message Encrytion and Decryption Project!


from cryptography.fernet import Fernet
import random

password="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
lng_password=int(input("Enter the length of the KEY :"))
a="".join(random.sample(password,lng_password))
print(f"\nYour KEY is :{a}")



def generate_key():
    return Fernet.generate_key()

def encrypt_message(key,message):
    cipher_suite=Fernet(key)
    encrypted_message=cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key,encrypted_message):
     cipher_suite=Fernet(key)
     decrypted_message=cipher_suite.decrypt(encrypted_message).decode()
     return decrypted_message



if __name__=="__main__":
    key=generate_key()
    message=input("\nEnter the message to Encrypt :")

    encrypted_message=encrypt_message(key,message)
    print(f"\nMessage is Encrypted to :{encrypted_message}")
    rahul=input("\nEnter the Key  to Decrypt :")
if rahul==a:
    decrypted_message=decrypt_message(key,encrypted_message)
    print(f"\nDecrypted message :{decrypted_message}")
else:
      print("\nIncorrect password. Message decryption failed.")
     


    
          

