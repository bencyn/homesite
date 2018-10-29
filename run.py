# local imports
from models import User, Comment

# Local variables
user = User()
comment = Comment()

def main():
    role = ''
    status = False
    username = null
    while True:
        print("""
        ----------------------------------------------------
       |                Welcome to HOMESITE                |
       | Help: List of commands for a better experience at |
       | Homesite 'We serve better than the competition    |
       | 'login' : Type this to login                      |
       | 'signup' : Type this to signup                    |
       | 'comment' :Type this to comment                   |
       | 'edit' : Type this to edit a comment              |
       | 'delete' : Type this to delete a comment,         |
        | 'quit' : To leave the program                    |
        | 'logout' : To logout of the site                 |
        | 'edit-own': To edit own                           |
       -----------------------------------------------------
        """)
        command = str(input("Enter a command? "))
        if command == "login":
            username = str(input("Enter your email: "))
            password = str(input("Enter your password"))
            if user.login(username, password):
                print("Logged in successfully")
                status = True
                command = str(input("Enter a command? "))
                role = user.login(username, password)
                if role == "admin":
                    print("Admin welcome")
                    username = username_
                    command = str(input("Enter a command? "))
                    if command == "delete":
                        comment_id = int(input("Enter the id of the comment you want to delete: "))
                        if comment.delete_comment(comment_id):
                            print("Comment deleted successfully")
                            command = str(input("Enter a command? "))
                        else: 
                            print("Comment of that id was not found, try another command to try again")
                            command = str(input("Enter command? "))
                    elif command == "edit":
                        comment_id = int(input("Enter the id of the comment you want to delete: "))
                        if comment.edit_comment(comment_id):
                            print("Comment updated successfully")
                            command = str(input("Enter a command? "))
                        else: 
                            print("Comment of that id was not found, try another command to try again")
                            command = str(input("Enter command? "))
                    elif command == "comment":
                        comment_msg = str(input("Enter the message you would like to comment: "))
                        comment__ = comment.create_comment(comment_msg, username)
                        print("""comment created successfully
                                    {}
                        """.format(comment__))
                        command = str(input("Enter a command? "))
                    else:
                        print("""
                        ------------Unfortunately we do not get your command--------------
                        ----------------------------------------------------
                        |                This are the commands accepted     |
                        | Help: List of commands for a better experience at |
                        | Homesite 'We serve better than the competition    |
                        | 'login' : Type this to login                      |
                        | 'signup' : Type this to signup                    |
                        | 'comment' :Type this to comment                   |
                        | 'edit' : Type this to edit a comment              |
                        | 'delete' : Type this to delete a comment,         |
                        | 'quit' : To leave the program                     |
                        | 'logout' : To logout of the site                  |
                        | 'edit-own': To edit own                           |
                        -----------------------------------------------------
                        """)
                        command = str(input("Try again by entering a command: "))
                elif role== "User":
                    print("User Welcome")
                    command = str(input("Enter a command? "))
                    if command == "comment":
                        comment_msg = str(input("Enter the message you would like to comment: "))
                        comment__ = comment.create_comment(comment_msg, username)
                        print("""comment created successfully
                                    {}
                        """.format(comment__))
                        command = str(input("Enter a command? "))
                    elif command =="edit-own":
                        print("Not yet handled")
                elif role== "moderator":
                    print("Moderator Welcome")
                    command = str(input("Enter a command? "))
                    if command == "delete":
                        comment_id = int(input("Enter the id of the comment you want to delete: "))
                        if comment.delete_comment(comment_id):
                            print("Comment deleted successfully")
                            command = str(input("Enter a command? "))
                        else: 
                            print("Comment of that id was not found, try another command to try again")
                            command = str(input("Enter command? "))   
                    else:
                        print("I am not getting you right now")
            else:
                print("Your role is not identified by the system try another command")
                command = str(input("Enter a command? "))
        elif command == "signup":
            username_ = str(input("Enter your new username: "))
            password = str(input("Enter your username: "))
            role_ = str(input("Enter your user role: ")).lower()
            status = True
            if user.signup(username_, password, role, status):
                print("Account succefully created")
                role = role_
                if role == "admin":
                    print("Admin welcome")
                    username = username_
                    command = str(input("Enter a command? "))
                    if command == "delete":
                        comment_id = int(input("Enter the id of the comment you want to delete: "))
                        if comment.delete_comment(comment_id):
                            print("Comment deleted successfully")
                            command = str(input("Enter a command? "))
                        else: 
                            print("Comment of that id was not found, try another command to try again")
                            command = str(input("Enter command? "))
                    elif command == "edit":
                        comment_id = int(input("Enter the id of the comment you want to delete: "))
                        if comment.edit_comment(comment_id):
                            print("Comment updated successfully")
                            command = str(input("Enter a command? "))
                        else: 
                            print("Comment of that id was not found, try another command to try again")
                            command = str(input("Enter command? "))
                    elif command == "comment":
                        comment_msg = str(input("Enter the message you would like to comment: "))
                        comment__ = comment.create_comment(comment_msg, username)
                        print("""comment created successfully
                                    {}
                        """.format(comment__))
                        command = str(input("Enter a command? "))
                    else:
                        print("""
                        ------------Unfortunately we do not get your command--------------
                        ----------------------------------------------------
                        |                This are the commands accepted     |
                        | Help: List of commands for a better experience at |
                        | Homesite 'We serve better than the competition    |
                        | 'login' : Type this to login                      |
                        | 'signup' : Type this to signup                    |
                        | 'comment' :Type this to comment                   |
                        | 'edit' : Type this to edit a comment              |
                        | 'delete' : Type this to delete a comment,         |
                        | 'quit' : To leave the program                     |
                        | 'logout' : To logout of the site                  |
                        | 'edit-own': To edit own                           |
                        -----------------------------------------------------
                        """)
                        command = str(input("Try again by entering a command: "))
                elif role== "User":
                    print("User Welcome")
                    command = str(input("Enter a command? "))
                    if command == "comment":
                        comment_msg = str(input("Enter the message you would like to comment: "))
                        comment__ = comment.create_comment(comment_msg, username)
                        print("""comment created successfully
                                    {}
                        """.format(comment__))
                        command = str(input("Enter a command? "))
                    elif command =="edit-own":
                        print("Not yet handled")
                elif role== "moderator":
                    print("Moderator Welcome")
                    command = str(input("Enter a command? "))
                    if command == "delete":
                        comment_id = int(input("Enter the id of the comment you want to delete: "))
                        if comment.delete_comment(comment_id):
                            print("Comment deleted successfully")
                            command = str(input("Enter a command? "))
                        else: 
                            print("Comment of that id was not found, try another command to try again")
                            command = str(input("Enter command? "))       
                    elif command== "comment":
                        comment_msg = str(input("Enter the message you would like to comment: "))
                        comment__ = comment.create_comment(comment_msg, username)
                        print("""comment created successfully
                                    {}
                        """.format(comment__))
                        command = str(input("Enter a command? "))
                    else:
                        print("""
                        ------------Unfortunately we do not get your command--------------
                        ----------------------------------------------------
                        |                This are the commands accepted     |
                        | Help: List of commands for a better experience at |
                        | Homesite 'We serve better than the competition    |
                        | 'login' : Type this to login                      |
                        | 'signup' : Type this to signup                    |
                        | 'comment' :Type this to comment                   |
                        | 'edit' : Type this to edit a comment              |
                        | 'delete' : Type this to delete a comment,         |
                        | 'quit' : To leave the program                     |
                        | 'logout' : To logout of the site                  |
                        | 'edit-own': To edit own                           |
                        -----------------------------------------------------
                        """)
                        command = str(input("Try again by entering a command: "))         
            else:
                print("""
                ---------------------------------
                Password: at least four characters
                """)
                command = str(input("Enter a command? "))
        else:
            print("""
            ------------Unfortunately we do not get your command--------------
             ----------------------------------------------------
            |                This are the commands accepted     |
            | Help: List of commands for a better experience at |
            | Homesite 'We serve better than the competition    |
            | 'login' : Type this to login                      |
            | 'signup' : Type this to signup                    |
            | 'comment' :Type this to comment                   |
            | 'edit' : Type this to edit a comment              |
            | 'delete' : Type this to delete a comment,         |
            | 'quit' : To leave the program                     |
            | 'logout' : To logout of the site                  |
            -----------------------------------------------------
            """)
            command = str(input("Try again by entering a command: "))