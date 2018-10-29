# local imports
from models import User, Comment

# Local variables
user = User()
comment = Comment()

def main():
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
       -----------------------------------------------------
        """)
        command = str(input("Enter a command? "))
        if command == "login":
            username = str(input("Enter your email: "))
            password = str(input("Enter your password"))
            if user.login(username, password):
                print("Logged in successfully")
                command = str(input("Enter a command? "))
            else:
                print("You do not have priviledges, try another command")
                command = str(input("Enter a command? "))
        elif command == "signup":
            username = str(input("Enter your new username: "))
            password = str(input("Enter your username: "))
            role = str(input("Enter your user role: "))
            status = True
            if user.signup(username, password, role, status):
                print("Account succefully created")
                command = str(input("Enter a command? "))
            else:
                print("You do not have priviledges, try another command")
                command = str(input("Enter a command? "))
        elif command == "comment":
            comment_msg = str(input("Enter the message you would like to comment: "))
            username = str(input("Enter your username: "))
            comment.create_comment(comment_msg, username)
            command = str(input("Enter a command? "))
        elif command == "logout":
            status = False
            user.logout(status)
            print("""
            Thank you for visitng homesite, we appreciate you
            """)
            command = "quit"
        elif command == "delete":
            comment_id = int(input("Enter the id of the comment you want to delete: "))
            if comment.delete_comment(comment_id):
                print("Comment deleted successfully")
                command = str(input("Enter a command? "))
            else:
                print("You do not have priviledges, try another command")
                command = str(input("Enter a command? "))                
        elif command == "edit":
            comment_id = int(input("Enter the comment_id you want to edit? "))
            if comment.edit_comment(comment_id):
                print("You edited the comment with the id {}".format(
                    comment_id
                ))
                command = str(input("Enter a command? "))
            else:
                print("You do not have priviledges, try another command")
                command = str(input("Enter a command? "))
        elif command == "quit":
            print("""
            | Hope to see you soon |
            """)
            break
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