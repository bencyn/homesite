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

    def logout(self):
        pass


class Comment(object):
    """handles comment CRUD Operations"""

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

