from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
'''
def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

master_password = input('Enter your master password: ')
key = load_key() + master_password.encode()
fer = Fernet(key)

def add_password():
    name = input('Account name: ')
    password = input('Password: ')
    with open('passwords.txt', 'a') as f:
        f.write(name + ' | ' + fer.encrypt(password.encode()).decode() + '\n')

def retrieve_password():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(' | ')
            print('User: ', user, ' | Password: ', fer.decrypt(passw.encode()).decode())

while True:
    mode = input('\nWould you like to add a new password or retrieve an existing one? (add/retrieve/quit): ').lower()
    if mode == 'quit':
        break
    elif mode == 'add':
        add_password()
    elif mode == 'retrieve':
        retrieve_password()
    else:
        print('Invalid mode. Please enter either "add" or "retrieve" or "quit".')
        continue