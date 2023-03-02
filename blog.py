class Blog:
    def __init__(self):
        self.users = set()
        self.posts = []
        self.current_user = None # attribute used to determine if there is a logged in user

    # Method to sign a new user up
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

    # Method to log a user in
    def log_user_in(self):
        # Get User credentials via input
        username = input('What is your username? ')
        password = input('What is your password? ')
        # Loop through each user in the blog
        for user in self.users:
            # Check if the user has that username AND the user's password is correct
            if user.username == username and user.check_password(password):
                # If user has correct credentials, set the blog's current_user to that user instance
                self.current_user = user
                print(f"{user} has logged in")
                break
        # If no users in our blog user set have that username/password, flash an invalid credentials message
        else:
            print("Username and/or password is incorrect.")

    # Method to log a user out
    def log_user_out(self):
        # Change the current_user attribute on this instance to None
        self.current_user = None
        print("You have successfully logged out.")

    # Method to create a new post if a user is logged in
    def create_new_post(self):
        # Check to make sure the user is logged in before creating a post
        if self.current_user is not None:
            # Get the title and body from user input
            title = input("Enter the title of your post: ")
            body = input("Enter the body of your post: ")
            # Create a new Post instance with input + logged in user
            new_post = Post(title, body, self.current_user)
            # Add the new post instance to our blog's list of posts
            self.posts.append(new_post)
            print(f"{new_post.title} has been created!")
        else:
            print("You must be logged in to perform this action.") # 401 Unauthorized



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
    id_counter = 1
    
    def __init__(self, title, body, author):
        """
        title: str
        body: str
        author: User
        """
        self.title = title
        self.body = body
        self.author = author
        self.id = Post.id_counter
        Post.id_counter += 1
        
    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"
    
    def __str__(self):
        formatted_post = f"""
        {self.id} - {self.title.title()}
        By: {self.author}
        {self.body}
        """
        return formatted_post



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
            print("1. Sign Up\n2. Log In\n5. Quit")
            # Ask the user which option they would like to do
            to_do = input('Which option would you like to do? ')
            # Keep asking if user chooses an invalid option
            while to_do not in {'1', '5', '2'}:
                to_do = input('Invalid Option. Please choose 1, 2, or 5 ')
            # if they choose 5, quit
            if to_do == '5':
                print("Thanks for checking out the blog")
                break
            elif to_do == '1':
                # Create a new user via the Blog create_new_user method
                my_blog.create_new_user()
            elif to_do == '2':
                # Call the log user in method from the blog
                my_blog.log_user_in()
        # if the current user is not None aka a user is logged in
        else:
            # Print menu options for logged in user
            print('1. Log Out\n2. Create New Post')
            to_do = input('Which option would you like to do? ')
            while to_do not in {'1', '2'}:
                to_do = input('Invalid Option. Please choose 1, 2 ')
            if to_do == '1':
                # Log the user out via the log_user_out method
                my_blog.log_user_out()
            elif to_do == '2':
                my_blog.create_new_post()


# Invoke the run_blog function to actually run the blog
run_blog()
