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
    """Defines comment objecta and methods"""

    def __init__(self):
        pass

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
