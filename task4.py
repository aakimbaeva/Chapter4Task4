class ContactList(list):
    def __init__(self, all_contacts):
        self.all_contacts = all_contacts

    def search_by_name(self, name):
        new_list = []
        for contact in self.all_contacts:
            if contact == name:
                new_list.append(contact)
        return new_list


all_contacts = ContactList(['Alice', 'Peter', 'Harry', 'Alice', 'Alice'])
print(all_contacts.search_by_name('Alice'))
