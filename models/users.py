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
            self.users.append({"id":id, "name":name, "email":email})

    def add_new_user(self, id, name, email):
        self.users.append({"id":id, "name":name, "email":email})

    def get_name_from_id(self, id):
        for user in self.users:
            if user["id"]==id:
                return user["name"]

    def if_id_exists(self, id):
        for user in self.users:
            if user["id"]==id:
                return True

    def save_to_json(self):
        with open("./data/student_data.json", "w") as outfile:
            json.dump(self.users, outfile)        

    