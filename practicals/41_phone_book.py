"""Program 3.5: dictionary-based phone book."""
phone_book = {'Yash': '9876543210', 'Dev': '9876543211', 'Manav': '9876543212', 'Raj': '9876543213', 'Vatsal': '9876543214'}
name = input('Search contact name: ')
print('Number:', phone_book.get(name, 'Contact not found'))
phone_book['Diya'] = '9999999999'
removed = phone_book.pop('Rohan')
print('Updated Diya number and removed Rohan:', removed)
for contact in sorted(phone_book):
    print(contact + ':', phone_book[contact])
