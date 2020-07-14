#
class User(Resource):
	def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404