from users.user import User

class PremiumUser(User):

    def __init__(self, name, email, dlc_num, username):
        super().__init__(name, email, dlc_num, username)