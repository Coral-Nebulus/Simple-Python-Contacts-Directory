#Contacts Directory

#Using def keyword to define the function, name & phone arguments are passed and linked by
#specifying that name is the key and its corresponding value is phone
def add_contact(name, phone, contacts):
    contacts[name] = phone
    print(f"Contact Added:  {name} - {phone}")
    return contacts

#Defining a search function that takes name & the directory as arguments
def search_contact(name, contacts):
  if name in contacts:
    print(f"{name}'s phone number is {contacts[name]}")
  else:
    print("This contact doesn't exist.")

#Defining function to delete a contact from the directory
#pop method is used. Del can also be used for this purpose
def del_contact(name, contacts):
  if name in contacts:
    contacts.pop(name)
    print(f"Contact deleted: {name}")
  else:
    print("Name not found")

#function to display contacts
def display_contacts(contacts):
  if len(contacts)==0:
    print("The contacts directory is empty")
  else:
    print("Contact List:")
    for i in contacts:
      print(f"{i}: {contacts[i]}")

#Creating an empty contacts dictionary
contacts_drty = {}

# making a program to display a menu & displaying results based on the user's input
menu_input =0
while menu_input !=5:
  print(" ")
  print("Contact Manager:")
  print("1. Add Contact")
  print("2. Search Contact")
  print("3. Delete Contact")
  print("4. Display Contacts")
  print("5. Exit")
  menu_input = int(input("Enter your choice, please:"))
  print(" ")

  if menu_input==1:
    name_input = str(input("Enter name: "))
    phone_input = str(input("Enter phone number: "))
    add_contact(name_input, phone_input, contacts_drty)

  elif menu_input ==2:
    search_input =str(input("Enter a name to search phone#: "))
    search_contact(search_input, contacts_drty)

  elif menu_input ==3:
    del_input = str(input("Enter a name to delete its contact: "))
    del_contact(del_input, contacts_drty)

  elif menu_input ==4:
    display_contacts(contacts_drty)

  elif menu_input ==5:
    print("Exiting Contact Manager. Ciao! Sayonara! Allah Hafiz")
    break
  else:
    print("Invalid input")
