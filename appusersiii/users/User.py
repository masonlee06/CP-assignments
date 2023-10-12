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
        new_post = f"{self.name}: {input('What would you like to post?: ')}"
        self.user_posts.append(new_post)
        User.post.append(new_post)
        
    @staticmethod
    def view_all_posts():
        for content in User.post:
            print(content)
    
    def view_user_posts(self):
        for content in self.user_posts:
            print(content)
