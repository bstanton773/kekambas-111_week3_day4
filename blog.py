class Blog:
    def __init__(self):
        self.users = set()
        self.posts = []
        self.current_user = None # attribute used to determine if there is a logged in user

    # Private method to get a post by its ID or return None if the post does not exist
    def __get_post_from_id(self, post_id):
        # Loop through all of the posts on the blog instance
        for post in self.posts:
            # If the post's id matches the post_id argument
            if post.id == post_id:
                # Return the post because we found the post with that ID
                return post
        return None

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

    # Method to view ALL posts
    def view_posts(self):
        # Check to see if there are any posts
        if self.posts:
            # Loop through all of the posts:
            for post in self.posts:
                # Display the post
                print(post)
        # If no posts
        else:
            print("There are currently no posts for this blog :(")

    # Method to view a SINGLE post by its ID
    def view_post(self, post_id):
        post = self.__get_post_from_id(post_id)
        if post:
            print(post)
        else:
            print(f"Post with an ID of {post_id} does not exist.") # 404 Not Found

    # Method to edit a post by ID
    def edit_post(self, post_id):
        post = self.__get_post_from_id(post_id)
        if post:
            # Check that the user is logged in AND that the logged in user is the author of the post
            if self.current_user is not None and self.current_user == post.author:
                # Print the post so the user can view it before they edit
                print(post)

                # Ask for the new edited title or have them enter skip to keep
                new_title = input('Please enter the new title or enter skip to keep the current title ')
                # if they don't enter skip
                if new_title != 'skip':
                    # Set the title attribute to the new_title
                    post.title = new_title
                # Same process for the body as title
                new_body = input('Please enter the new body of the post or enter skip to keep the current body ')
                if new_body != 'skip':
                    post.body = new_body

                print(f"{post.title} has been updated!")

            # Else if the user is logged in but NOT the author
            elif self.current_user is not None and self.current_user != post.author:
                print("You do not have permission to edit this post") # 403 Forbidden
            # If user not logged in at all
            else:
                print("You must be logged in to perform this action") # 401 Unauthorized
        else:
            print(f"Post with an ID of {post_id} does not exist.") # 404 Not Found

    # Method to delete a post by its ID
    def delete_post(self, post_id):
        post = self.__get_post_from_id(post_id)
        if post:
            # Check that the user is logged in AND that the logged in user is the author of the post
            if self.current_user is not None and self.current_user == post.author:
                print(post)
                you_sure = input("Are you sure you want to delete this post? This action cannot be undone. Enter 'yes' to delete. ")
                if you_sure == 'yes':
                    self.posts.remove(post)
                    print(f"{post.title} has been removed from the blog.")
                else:
                    print("Okay. We won't delete the post.")
            # Else if the user is logged in but NOT the author
            elif self.current_user is not None and self.current_user != post.author:
                print("You do not have permission to delete this post") # 403 Forbidden
            # If user not logged in at all
            else:
                print("You must be logged in to perform this action") # 401 Unauthorized
        else:
            print(f"Post with an ID of {post_id} does not exist.") # 404 Not Found


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
            print("1. Sign Up\n2. Log In\n3. View All Posts\n4. View Single Post\n5. Quit")
            # Ask the user which option they would like to do
            to_do = input('Which option would you like to do? ')
            # Keep asking if user chooses an invalid option
            while to_do not in {'1', '5', '2', '3', '4'}:
                to_do = input('Invalid Option. Please choose 1, 2, 3, 4 or 5 ')
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
            elif to_do == '3':
                # Call the view_posts method
                my_blog.view_posts()
            elif to_do == '4':
                # Get the id of the post 
                post_id = input('What is the id of the post you would like to view? ')
                # if the post_id is not a digit, continue to ask them to fix it
                while not post_id.isdigit():
                    post_id = input('Invalid ID. Must be an integer. Please enter the ID again: ')
                # Call the view single post method with post_id as an argument
                my_blog.view_post(int(post_id))
        # if the current user is not None aka a user is logged in
        else:
            # Print menu options for logged in user
            print('1. Log Out\n2. Create New Post\n3. View All Posts\n4. View Single Post\n5. Edit A Post\n6. Delete A Post')
            to_do = input('Which option would you like to do? ')
            while to_do not in {'1', '2', '3', '4', '5', '6'}:
                to_do = input('Invalid Option. Please choose 1, 2, 3, 4, 5, or 6 ')
            if to_do == '1':
                # Log the user out via the log_user_out method
                my_blog.log_user_out()
            elif to_do == '2':
                my_blog.create_new_post()
            elif to_do == '3':
                # Call the view_posts method
                my_blog.view_posts()
            elif to_do == '4':
                # Get the id of the post 
                post_id = input('What is the id of the post you would like to view? ')
                # if the post_id is not a digit, continue to ask them to fix it
                while not post_id.isdigit():
                    post_id = input('Invalid ID. Must be an integer. Please enter the ID again: ')
                # Call the view single post method with post_id as an argument
                my_blog.view_post(int(post_id))
            elif to_do == '5':
                # Get the id of the post 
                post_id = input('What is the id of the post you would like to edit? ')
                # if the post_id is not a digit, continue to ask them to fix it
                while not post_id.isdigit():
                    post_id = input('Invalid ID. Must be an integer. Please enter the ID again: ')
                # Call the edit post method with post_id as an argument
                my_blog.edit_post(int(post_id))
            elif to_do == '6':
                # Get the id of the post 
                post_id = input('What is the id of the post you would like to delete? ')
                # if the post_id is not a digit, continue to ask them to fix it
                while not post_id.isdigit():
                    post_id = input('Invalid ID. Must be an integer. Please enter the ID again: ')
                # Call the edit post method with post_id as an argument
                my_blog.delete_post(int(post_id))


# Invoke the run_blog function to actually run the blog
run_blog()
