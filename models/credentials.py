import json
from cryptography.fernet import Fernet

class Credentials():
    def __init__(self):

        with open('./data/login_credentials.json') as fp:
            data = json.load(fp)
        self.credentials = []

        for index in range(len(data)):
            id = data[index]["id"]
            key = data[index]["key"]
            fernet = Fernet(key.encode('utf-8'))
            encPassword = data[index]["password"].encode('utf-8')
            password = fernet.decrypt(encPassword).decode()            
            self.credentials.append({"id":id,"password":password,"key":key})


    def if_credentials_exist(self, id, password):
        
        flag = False

        for credential in self.credentials:
            if credential["id"]==id and credential["password"]==password:
                flag = True
        
        return flag

    def if_id_exists(self, id):

        flag = False

        for credential in self.credentials:
            if credential["id"]==id:
                flag = True
        
        if flag == True:
            return "yes"
        else:
            return "no"

    def get_name_from_id(self, id):
        with open('./data/student_data.json') as fp:
            data = json.load(fp)
        for index in range(len(data)):
            if data[index]["id"]==id:
                return data[index]["name"]

    def save_credentials(self, id, password):
        key = Fernet.generate_key()
        self.credentials.append({"id":id,"password":password,"key":key.decode('utf-8')})

    def print_credentials(self):
        for credential in self.credentials:
            print(credential)

    def encrypt_credentials(self):
        encrypted_credentials = []
        for credential in self.credentials:
            encryped_credential = {}
            encryped_credential["id"]=credential["id"]
            fernet = Fernet(credential["key"].encode('utf-8'))
            encryped_credential["password"] = fernet.encrypt(credential["password"].encode()).decode('utf-8')
            encryped_credential["key"] = credential["key"]
            encrypted_credentials.append(encryped_credential)
        return encrypted_credentials

    def save_to_json(self, credentials):
        with open("data/login_credentials.json", "w") as outfile:
            json.dump(credentials, outfile)



