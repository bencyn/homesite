from datetime import date

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


    def login(self,username,password):
        current_date = str(date.today())
        current_user=[user for user in users if user['username']==username]
        if current_user:
            user_password=current_user[0]['password']
            if user_password==password:
                current_user[0]['status']=True
                current_user[0]['login_time']=current_date
                user_role=current_user[0]['role']
                return user_role
            return None
	    
        return None

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

