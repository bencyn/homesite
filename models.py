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
        self.comments_list = []
        self.users = []

    def create_comment(self, message, username):
        """ add comment """
        for user in self.users:
            if user['username'] == username:
                if user['status'] is True: 
                    incremented_id = len(self.comments_list) + 1
                    timestamp = datetime.datetime.now()
                    comment = {
                    "id": incremented_id,
                    "message": message, 
                    "timestamp":timestamp,
                    "author":username
                    }
                    self.comments_list.append(comment)
            return " you must be logged in to make comment"
        return "user does not exist"

    def create_comment(self):
        pass

    def edit_comment(self, id):
        new = input('edit the message')
        for comment in self.comments:
            if comment['id'] == id:
                comment.update(new)


    def delete_comment(self, id):
        for i, comment in enumerate(self.comments):
            if orcomment['id'] == id:
                self.comments.pop(i)
