# Day 92 Project: Contact Book

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name: str, phone: str, email: str):
        self.contacts[name.lower()] = {"name": name, "phone": phone, "email": email}

    def search(self, query: str):
        q = query.lower()
        return [c for k, c in self.contacts.items() if q in k or q in c["email"]]

book = ContactBook()
book.add("Thanusha Simran", "123-456-7890", "thanusha@example.com")
book.add("Alex Morgan", "987-654-3210", "alex@example.com")
print("Search results for 'thanusha':", book.search("thanusha"))
