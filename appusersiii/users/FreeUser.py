from users.user import User

class FreeUser(User):

    def __init__(self, name, email, dlc_num, username):
        super().__init__(name, email, dlc_num, username)

    def make_post(self):
        if len(self.user_posts) > 1:
            print('Maximum posts reached for free user.')
        else:
            user_input = input('What would you like to post?: ')
            new_post = f'{self.name}: {user_input}'
            self.user_posts.append(new_post)
            User.post.append(new_post)

# mason = FreeUser('Mason', 'stuff@stuff.org', 651561, 'masonlee')

# mason.make_post()
# mason.make_post()
# mason.make_post()