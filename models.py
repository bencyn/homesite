import datetime

users = []
comments = []


class User(object):
    """"Defines user objects and methods"""

    def __init__(self):
        self.all_users=users

    def signup(self, username, password, login_time=None,role=None, status=True):
        
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
        current_date = str(datetime.datetime.utcnow())
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

    def create_comment(self, message, username):
        """ add comment """
        for user in users:
            print(users)
            if user['username'] == username:
                if user['status'] is True: 
                    incremented_id = len(comments) + 1
                    timestamp = datetime.datetime.utcnow()
                    comment = {
                    "id": incremented_id,
                    "message": message, 
                    "timestamp":timestamp,
                    "author":username
                    }
                    comments.append(comment)
                    return comment
                return None
            return None
        return None

    def edit_comment(self, id):
        new = input('edit the message')
        for comment in comments:
            if comment['id'] == id:
                comment.update(new)


    def delete_comment(self, id):
        for i, comment in enumerate(comments):
            if comment['id'] == id:
                comments.pop(i)
