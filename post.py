#
def post(self, name):
    parser = reqparse.RequestParser()
    parser.add_argument("age")
    parser.add_argument("occupation")
    args = parser.parse_args()

    for user in users:
        if(name == user["name"]):
            return "User with name {} already exists".format(name), 400

    user = {
        "name": name,
        "age": args["age"],
        "occupation": args["occupation"]
    }
    users.append(user)
    return user, 201