class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated(function):
    """It executes the function if the value of 'is_logged_in' attribute is set to True"""

    def wrapper(*args, **kwargs):
        # here, 'args[0]' is 'user' parameter
        if args[0].is_logged_in == True:
            # only because the 'is_logged_in' attribute is set to true, the function is being executed
            function(args[0])

    return wrapper


@is_authenticated
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Shrijan")
new_user.is_logged_in = True
create_blog_post(new_user)
