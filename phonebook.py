from asyncio import selector_events


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
        
    elif selected_option == "1":
        name = ("what contact's number would you like?")
        print(phonebook[name])
        # print(menu)
    
    if selected_option == "5":
        quit(selected_option)
   
  
