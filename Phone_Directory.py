import os
import json


# Function to read records from the file
def read_records():
    records = []
    if os.path.exists("phonebook.json"):
        with open("phonebook.json", "r") as file:
            records = json.load(file)
    return records


# Function to write records to the file
def write_records(records):
    with open("phonebook.json", "w") as file:
        json.dump(records, file)


# Function to print menu
def print_menu():
    print("\nPhonebook")
    print("1. Display all records")
    print("2. Add a new record")
    print("3. Edit a record")
    print("4. Search records")
    print("5. Exit")


# Function to print records
def print_records(records, page_num, records_per_page):
    start_index = (page_num - 1) * records_per_page
    end_index = min(start_index + records_per_page, len(records))

    if start_index >= end_index:
        print("No records to display.")
        return

    print("\nPhonebook (Page", page_num, ")")
    for i in range(start_index, end_index):
        print(f"{i + 1}. {' | '.join(records[i])}")


# Function to add a new record
def add_record():
    surname = input("Enter surname: ")
    name = input("Enter name: ")
    patronymic = input("Enter patronymic: ")
    organization = input("Enter organization name: ")
    work_phone = input("Enter work phone: ")
    personal_phone = input("Enter personal phone (cell): ")

    new_record = [surname, name, patronymic, organization, work_phone, personal_phone]
    records.append(new_record)
    write_records(records)
    print("Record added successfully!")


# Function to edit a record
def edit_record():
    print_records(records)
    choice = int(input("Enter the number of the record you want to edit: "))
    if choice < 1 or choice > len(records):
        print("Invalid choice")
        return
    record = records[choice - 1]
    print("Selected record:", ' | '.join(record))
    field = int(input("Enter the number of the field you want to edit: "))
    if field < 1 or field > 6:
        print("Invalid field choice")
        return
    new_value = input("Enter the new value: ")
    record[field - 1] = new_value
    write_records(records)
    print("Record edited successfully!")


# Function to search records
def search_records():
    search_term = input("Enter a string to search: ")
    found_records = []
    for record in records:
        if any(search_term.lower() in field.lower() for field in record):
            found_records.append(record)
    print_records(found_records, 1, len(found_records))


# Main part of the program
while True:
    print_menu()
    choice = input("Enter your choice: ")
    records = read_records()

    if choice == "1":
        page_num = 1
        records_per_page = 5  # Set your desired number of records per page
        while True:
            print_records(records, page_num, records_per_page)
            next_action = input("Press Enter to continue or type 'q' to quit: ")
            if next_action.lower() == 'q':
                break
            page_num += 1
    elif choice == "2":
        add_record()
    elif choice == "3":
        edit_record()
    elif choice == "4":
        search_records()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
