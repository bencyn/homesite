users = []
comments = []


class User(object):
    """"Defines user objects and methods"""

    def __init__(self):
        self.all_users=users

    def signup(self, username, password, login_time=None,role=None, status=None,):
        
        new_user = {
            "username": username,
            "password": password,
            "role": role,
            "status": status,
            "login_time":login_time
        }

        users.append(new_user)
        user_name=new_user['username']
        return user_name


    def login(self):
        pass

    def logout(self):
        pass


class Comment(object):
    """Defines comment objects and methods"""

    def __init__(self):
        pass

    def create_comment(self):
        pass

    def edit_comment(self):
        pass

    def delete_comment(self):
        pass

