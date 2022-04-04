from ast import Delete
from asyncio import selector_events
from os import remove
from tkinter import N


phonebook = {}

menu = """

Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit

"""

print(menu)

selected_option = input("What do you want to do (1-5)")


while selected_option != "5":
    print(menu)
    selected_option = input("What do you want to do (1-5)")


    if selected_option == "2": 
        name = input("What is the contact's name?")
        phone_number = input("what is their phone number")
        phonebook[name] = phone_number
        print("contact saved successfully!")
        
    if selected_option == "1":
        name = input("who are you looking for?") #changed the wording of the string 
        phonebook.get(name) 
        print(phonebook.get(name))
        
    elif  phonebook == (None):      #created an "elif" function fot 'none' to be equivalant to a string
        print("Data not Found")
        
    
    if selected_option == "5":
        quit(selected_option)
    
    
    if selected_option == "3":
        name = input("What contact's number are you trying to delete?")
        phonebook.pop(phonebook[name])      # tacking out phone_number that was next to "name"
        print(phonebook)
    
    if selected_option == "4":
        print(phonebook)

        

        

   
  
