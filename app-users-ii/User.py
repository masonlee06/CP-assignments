class User:
    post = []
    
    def __init__(self, name, email, dlc_num, username):
        self.name = name
        self.email = email
        self.dlc_num = dlc_num
        self.username = username
        self.user_posts = []
        
    
    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nUsername: {self.username}\nDriver's License Number: {self.dlc_num}"
    
    def make_post(self):
        user_input = input('What would you like to post?: ')
        new_post = f'{self.name}: {user_input}'
        self.user_posts.append(new_post)
        User.post.append(new_post)
        
    @staticmethod
    def view_all_posts():
        for content in User.post:
            print(content)
    
    def view_user_posts(self):
        for content in self.user_posts:
            print(content)

mason = User('Mason', 'mason@stuff.org', 23423423, 'masonlee06')
regis = User('Regis', 'regis@stuff.com', 1423452, 'regi')

# mason.make_post()
mason.make_post()
regis.make_post()
regis.make_post()
regis.make_post()
mason.view_user_posts()
# regis.view_user_posts()
# User.view_all_posts()

