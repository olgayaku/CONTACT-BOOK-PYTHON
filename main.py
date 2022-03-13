print("Welcome to the telephone book")

from tabulate import tabulate
import json

with open("Contacts.json","w") as json_file:
    dataToJson = {"contacts":[{
        "Name": "Michael",
        "LastName": "Koen",
        "Address": "Jerusalem",
        "Phone": "111111"
    },
    {
        "Name": "Daniel",
        "LastName": "Shvarz",
        "Address": "Kiev",
        "Phone": "222222"
    },
    {
        "Name": "David",
        "LastName": "Kaz",
        "Address": "Haifa",
        "Phone": "333333"

    }]}
    json.dump(dataToJson, json_file, indent=4)
    json_file.close()
def list():
   with open("Contacts.json") as json_file:
       json_file_data = json_file.read()
       our_json_data = json.loads(json_file_data)
       print(tabulate(our_json_data["contacts"],headers="keys", tablefmt="grid"))
def add():
    with open("Contacts.json") as json_file:
        json_file_data = json_file.read()
        our_json_data = json.loads(json_file_data)
        print("Name:")
        name = input()
        print("LastName:")
        lastname = input()
        print("Address:")
        address = input()
        print("Phone:")
        phone = input()
        new_contact = {"Name": name,
               "LastName": lastname,
               "Address": address,
               "Phone": phone}
        our_json_data["contacts"].append(new_contact)
    with open("Contacts.json", "w") as json_file:
        json.dump(our_json_data,json_file,indent=4)
        print("You are added new contact")
def search():
    print("Print the name of the contact:")
    name = input("> ")
    with open("Contacts.json") as json_file:
        json_file_data = json_file.read()
        our_json_data = json.loads(json_file_data)
    for x in our_json_data["contacts"]:
        if x["Name"] == name:
             print("", "Name: ", x["Name"], '\n', "Lastname:", x["LastName"], '\n',"Address:", x["Address"], '\n', "Phone:", x["Phone"])
             break
    else:
        print("The contact was not found")
def edit():
    print("Print the name of the contact that you want to edit:")
    name = input("> ")
    with open("Contacts.json") as json_file:
        json_file_data = json_file.read()
        our_json_data = json.loads(json_file_data)

    for x in our_json_data["contacts"]:
        if x["Name"] == name:
            print("Enter new name: ")
            new_name = input("> ")
            x["Name"] = new_name
            print("Enter new lastname: ")
            new_lastname = input("> ")
            x["LastName"] = new_lastname
            print("Enter new address: ")
            new_address = input("> ")
            x["Address"] = new_address
            print("Enter new phone number: ")
            new_phone = input("> ")
            x["Phone"] = new_phone
            with open("Contacts.json", "w") as json_file:
                json.dump(our_json_data, json_file, indent=4)
            break
    else:
        print("The contact was not found")
def delete():
    print("Please enter the name: ")
    name = input('> ')
    with open("Contacts.json") as json_file:
        json_file_data = json_file.read()
        our_json_data = json.loads(json_file_data)
    for i in range(len(our_json_data["contacts"])):
        if our_json_data["contacts"][i]["Name"] == name:
            our_json_data["contacts"].pop(i)
            with open("Contacts.json", "w") as json_file:
                 json.dump(our_json_data, json_file, indent=4)
            break
    else:
        print("The contact was not found")

def reset():
    with open("Contacts.json") as json_file:
        json_file_data = json_file.read()
        our_json_data = json.loads(json_file_data)
    while our_json_data["contacts"]:
        our_json_data["contacts"].pop(0)
    with open("Contacts.json", "w") as json_file:
        json.dump(our_json_data, json_file, indent=4)

    print("Ok, you did reset all contacts ")
try:
    while True:
               print("1. Add new contact\n2. View contacts\n3. Search contacts\n4. Update contact\n5. Delete contact\n6. Reset all\n7. Exit")
               print("\nChoose: ")
               command = input('> ')
               if command == '1':
                 add()
               elif command == '2':
                   list()
               elif command == '3':
                   search()
               elif command == '4':
                   edit()
               elif command == '5':
                   delete()
               elif command == '6':
                   reset()
               elif command == '7':
                  break
               else:
                    print("Invalid choice")
except Exception as error:
    print(error+"Create Contacts.json file")