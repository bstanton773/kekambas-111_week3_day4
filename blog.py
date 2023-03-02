class Blog:
    def __init__(self):
        self.users = set()
        self.posts = []
        self.current_user = None # attribute used to determine if there is a logged in user

    def create_new_user(self):
        # Get user info from input
        username = input('Please enter a username: ')
        # Check if there is a user that already has that username
        if username in {u.username for u in self.users}:
            print(f"User with username {username} already exists.")
        # if not, create new user
        else:
            # Get the password
            password = input('Please enter a password: ')
            # Create a new User instance with info from the inputs
            new_user = User(username, password)
            # Add the new User instance to our blog user set
            self.users.add(new_user)
            print(f"{new_user} has been created!")



class User:
    id_counter = 1
    
    def __init__(self, username, password):
        self.username = username
        self.password = password[::-2]
        self.id = User.id_counter
        User.id_counter += 1
        
    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f"<User {self.id}|{self.username}>"
    
    def check_password(self, password_guess):
        return self.password == password_guess[::-2]



class Post:
    pass



# define a function to run the blog
def run_blog():
    print('Welcome to the blog. I hope you like it!')
    # Create an instance of the Blog Class
    my_blog = Blog()
    # Keep looping while the blog is "running"
    while True:
        # if there is no current user logged in
        if my_blog.current_user is None:
            # Print the menu options for logged out users
            print("1. Sign Up\n5. Quit")
            # Ask the user which option they would like to do
            to_do = input('Which option would you like to do? ')
            # Keep asking if user chooses an invalid option
            while to_do not in {'1', '5'}:
                to_do = input('Invalid Option. Please choose 1 or 5 ')
            # if they choose 5, quit
            if to_do == '5':
                print("Thanks for checking out the blog")
                break
            elif to_do == '1':
                # Crate a new user via the Blog create_new_user method
                my_blog.create_new_user()


# Invoke the run_blog function to actually run the blog
run_blog()
