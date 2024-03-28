class PhoneDirectory:
    def __init__(self):
        self.directory = []

    def add_entry(self, name,ph_num, place):
        if not self.check_phonenum(ph_num):
            raise ValueError("Phone number must be 10 digits long.")
        self.directory.append({"Name": name, "Phone Number": ph_num, "Place": place})

    def check_phonenum(self, ph_num):
        return ph_num.isdigit() and len(ph_num) == 10

    def search_by_name(self, name):
        results = [entry for entry in self.directory if entry["Name"].lower() == name.lower()]
        return results

    def display_directory(self):
        for entry in self.directory:
            print(f"Name: {entry['Name']}, Phone Number: {entry['Phone Number']}, Place: {entry['Place']}")
            
    def hard_copy(self):
        file_path = "xyz.txt"
        if not self.check_file():
            print(f"Creating file: {file_path}")
            with open(file_path, 'w') as file:
                print("File created successfully.")
        else:
            print(f"File already exists: {file_path}")
        
        with open(file_path, "w") as file:
            for entry in self.directory:
                file.write(f"Name: {entry['Name']}, Phone Number: {entry['Phone Number']}, Place: {entry['Place']}\n")
        print("Directory copied to file successfully.")

    
    def check_file(self):
        file_path = "xyz.txt"
        try:
            with open(file_path, 'r') as file:
               print(f"File found: {file_path}")
               file.close()
            return True
        except FileNotFoundError:
            print(f"File not found: {file_path}.")
            return False
        


def main():
    directory = PhoneDirectory()

    while True:
        print("\nPhone Directory")
        print("1. Add New Entry")
        print("2. Search by Name")
        print("3. Display All Entries")
        print("4. Get Hardcopy")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            ph_num = input("Enter phone number (10 digits): ")
            place = input("Enter place: ")
            try:
                directory.add_entry(name,ph_num, place)
                print("Entry added successfully.")
            except ValueError as x:
                print(f"Error: {x}")
        
        elif choice == "2":
            name = input("Enter name to search: ")
            results = directory.search_by_name(name)
            if results:
                for entry in results:
                    print(f"Name: {entry['Name']}, Phone Number: {entry['Phone Number']}, Place: {entry['Place']}")
            else:
                print("No entries found.")
        
        elif choice == "3":
            directory.display_directory()
            
        elif choice == "4":
            directory.hard_copy()
            
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
