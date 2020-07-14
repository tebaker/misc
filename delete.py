def delete(self, name):
    global users
    users = [user for user in users if user["name"] != name]
    return "{} is deleted.".format(name), 200