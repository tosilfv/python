# ADVANCED DECORATORS PRACTISE
import time

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def login_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
        else:
            fail_text()
    return wrapper

def wait_text():
    print("Checking Credentials, Please Wait...")
    time.sleep(1)

def fail_text():
    print("Login Failed.")

@login_decorator
def welcome_text(user):
    print(f"Hello user {user.name}")

user_admin = User("Admin")
user_admin.is_logged_in = True
wait_text()
welcome_text(user_admin)
