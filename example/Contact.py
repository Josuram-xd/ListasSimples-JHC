class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.next = None

class ContactList:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def add_contact(self, contact):
        if self.first_node is None:
            self.first_node = contact
            self.last_node = contact
        else:
            self.last_node.next = contact
            self.last_node = contact

    def print_contacts(self):
        if self.first_node is None:
            print("No contacts in the list.")
        else:
            current_node = self.first_node
            while current_node is not None:
                print(f"Name: {current_node.name}")
                print(f"Email: {current_node.email}")
                print(f"Phone: {current_node.phone}")
                print(f"Next: {current_node.next}")
                print("--------------------")
                current_node = current_node.next