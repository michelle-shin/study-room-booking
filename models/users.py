import json

class Users():
    def __init__(self):
        self.users = []
                
        with open('./data/student_data.json') as fp:
            data = json.load(fp)
        for index in range(len(data)):
            name = data[index]["name"]
            email = data[index]["email"]
            id = data[index]["id"]
            approved = data[index]["approved"]
            self.users.append({"id":id, "name":name, "email":email, "approved":approved})

    def add_new_user(self, id, name, email):
        # self.users.append({"id":id, "name":name, "email":email, "approved":"no"})
        self.users.append({"id":id, "name":name, "email":email, "approved":"yes"})

    def get_name_from_id(self, id):
        for user in self.users:
            if user["id"]==id:
                return user["name"]
    
    def get_email_from_id(self, id):
        for user in self.users:
            if user["id"]==id:
                return user["email"]            

    def if_id_exists(self, id):
        for user in self.users:
            if user["id"]==id:
                return True

    def if_not_approved(self, id):
        for user in self.users:
            if user["id"]==id and user["approved"]=="no":
                return True

    def approve_account(self, id):
        for user in self.users:
            if user["id"]==id:
                user["approved"]=="yes"
        self.save_to_json()

    def save_to_json(self):
        with open("./data/student_data.json", "w") as outfile:
            json.dump(self.users, outfile)        

    