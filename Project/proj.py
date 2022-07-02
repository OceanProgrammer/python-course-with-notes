import json, os

class ContactBook:
    data = {}

    def add(self,name, phone, email):
        self.data[name] = phone, email # tuple
        
    def edit(self,name, newPhone, newEmail):
        self.data[name] = newPhone, newEmail
    def delete(self,name):
        self.data.pop(name)
    def view(self):
        os.startfile('data.json')

book = ContactBook()
print(book.data)
book.add("Bill", 9876543210, 'billishere@gmail.com')
book.add("Bill2", 9876543210, 'billishere@gmail.com')
print(book.data)
book.delete('Bill')
print(book.data)
book.edit('Bill', 1234567890, 'billisalive@outlook.com')
print(book.data)

with open('data.json', 'w') as f:
    json.dump(book.data, f)

book.view()