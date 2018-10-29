users = []
comments = []


class User(object):
    """"Defines user objects and methods"""

    def __init__(self):
        pass

    def signup(self):
        pass

    def login(self):
        pass

    def logout(self, username):
        """this method sign's out a user"""

        current_user = [user for user in users if user["username"] == username]

        if not current_user:
            return None
        elif user[0]["status"] == False:
            return None
        else:
            for user in users:
                if user["username"] == username:
                    user["status"] =False 
                    return username



class Comment(object):
    """Defines comment objecta and methods"""

    def __init__(self):
        pass

    def create_comment(self):
        pass

    def edit_comment(self):
        pass

    def delete_comment(self):
        pass

