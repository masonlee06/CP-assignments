class ContactList:

    

    def __init__(self, contacts=[], info=[]):
        self._contacts = contacts
        self.info = info
        sorted_info = sorted(self.info)
    
    def __repr__(self):
        return f'{self.get_contacts}: {self.info}'


    @property
    def get_contacts(self):
        return self._contacts
    
    @get_contacts.setter
    def set_contacts(self, new_name):
        self._contacts = new_name

    @staticmethod
    def find_shared_contacts(list_name, compared_list):
        pass

    def add_contact(self):
        name = input("Enter name: ")
        number = input("Enter number: ")
        new_contact = {'name':f'{name}','number':f'{number}'}
        self.info.append(new_contact)

friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_list = ContactList('friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

print(my_list)

my_list.add_contact()

print(my_list)